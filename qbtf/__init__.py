import shutil
import pyrebase
from mcdreforged.api.all import *
from qbtf.config import *
from qbtf.UI import *
import os

conf = Configure
out_path = conf.dest_path+conf.comp_name #It defines the path where the zip file will be saved
unknown_argument_msg = gen_unknown_argument_message()

def print_msg(server: PluginServerInterface, msg: str, prefix='[QBTF] '):
	msg = RTextList(prefix, msg)
	server.get_server().logger.info(msg)
	server.get_server().say(msg)

def check_folder(server: PluginServerInterface): #It checks if the folder exists, if not, it creates it.
	if not os.path.exists(conf.dest_path):
		os.makedirs(conf.dest_path)
		server.logger.info("dest_path folder created")

def compress_qb(server: PluginServerInterface): #It compresses the source code of the plugin into a zip file.
	print_msg(server, "§a[+]§r §3Compressing...§r")
	try:
		shutil.make_archive(out_path, conf.extension, conf.source_path)
		print_msg(server, "§a[+]§r DONE")
	except Exception as error:
		print_msg(server, "§c[-]§r Epic fail")
		server.get_server().logger.exception("ERROR while compressing the plugin")

#TODO: remove slot1 content, and put the qb_comp content in the slot1
def extract_qb(server: PluginServerInterface): #It extracts the source code of the plugin from the zip file.
	print_msg(server, "§a[+]§r §3Extracting...§r")
	try:
		shutil.unpack_archive(conf.comp_name + conf.extension, conf.source_path, conf.extension)
		print_msg(server, "§a[+]§r DONE")
	except:
		print_msg(server, "§c[-]§r Epic fail")


def upload_to_firebase(server: PluginServerInterface): #It uploads the zip file to Firebase Storage
    print_msg(server, "§a[+]§r §3Uploading to Firebase...§r")
    try:
        firebase = pyrebase.initialize_app(conf.firebase_config)
        storage = firebase.storage()
        file = out_path +"."+ conf.extension
        server.get_server().logger.info(file)
        cloudfilename = (conf.fb_path + conf.comp_name +"."+ conf.extension)
        server.get_server().logger.info(cloudfilename)
        storage.child(cloudfilename).put(file)
        os.remove(file)
        print_msg(server, "§a[+]§r DONE")
    except KeyError:
        print_msg(server, "§c[-]§r ERROR")
        print_msg(server, "§c[-]§r You must fill the 'firebase_config' field in the plugin configuration file.")

def download_from_firebase(server: PluginServerInterface): #It downloads the zip file from Firebase Storage
    print_msg(server, "§a[+]§r §3Downloading from Firebase...§r")
    try:
        firebase = pyrebase.initialize_app(conf.firebase_config)
        storage = firebase.storage()
        file = conf.comp_name + conf.extension
        cloudfilename = (conf.fb_path + file)
        storage.child(cloudfilename).download(file)
        print_msg(server, "§a[+]§r DONE")
    except KeyError:
        print_msg(server, "§c[-]§r ERROR")
        print_msg(server, "§c[-]§r You must fill the 'firebase_config' field in the plugin configuration file.")

def upload():
  compress_qb()
  upload_to_firebase()

def download():
  download_from_firebase()
  extract_qb()

#|REGISTER COMMANDS|    
def register_command(server: PluginServerInterface):
  def get_literal_node(literal):
    lvl = conf.permission
    return Literal(literal).requires(lambda src: src.has_permission(lvl)).on_error(RequirementNotMet, lambda src: src.reply("Permission denied"), handled=True)

  server.register_command(
    Literal(conf.prefix).
      runs(lambda src: src.reply(gen_help_message())).
        on_error(UnknownArgument, lambda src, _: print_msg(server, unknown_argument_msg), handled=True).
          then(
            get_literal_node('upload').runs(lambda src, ctx: upload())
            ).
          then(
            get_literal_node('download').runs(lambda src, ctx: download())
          )
    )

#TODO: add !!qbtf upload and !!qbtf download commands using .then()
def on_load(server: PluginServerInterface, old_module):
  global conf #do conf global
  check_folder(server) #check folder
  conf = server.load_config_simple('config.json', target_class=Configure) #load config.json file to conf
  msg = 'Plugin qbtf loaded, use {}'.format(conf.prefix) #message showed when server start
  server.logger.info(msg) #displays message
  register_command(server) #register command
  server.register_help_message(conf.prefix, {'en_us': help_message}) # when !!help it shows help message
