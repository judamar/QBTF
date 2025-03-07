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
    server.logger.info(msg)
    server.say(msg)

@new_thread("QBTF Check Folder")
def check_folder(server: PluginServerInterface): #It checks if the folder exists, if not, it creates it.
    if not os.path.exists(conf.dest_path):
        os.makedirs(conf.dest_path)
        server.logger.info("dest_path folder created")

def compress_qb(server: PluginServerInterface): #It compresses the source code of the plugin into a zip file.
    print_msg(server, f"§a[+]§r Compressing {conf.source_path}")
    try:
        shutil.make_archive(out_path, conf.extension, conf.source_path)
        print_msg(server, "§a[+]§r Success§r")
    except Exception as error:
        print_msg(server, f"§c[-] Compression failed§r {error}")

def extract_qb(server: PluginServerInterface): #It extracts the source code of the plugin from the zip file.
    print_msg(server, f"§a[+]§r Extracting")
    try:
        shutil.rmtree(conf.source_path)
        os.makedirs(conf.source_path)
        shutil.unpack_archive(conf.dest_path + conf.comp_name + '.' + conf.extension, conf.source_path, conf.extension)
        os.remove(out_path +"."+ conf.extension)
        print_msg(server, "§a[+]§r Success")
        print_msg(server, f"§a[+]§r Ready to restore the {conf.source_path}")
    except Exception as error:
        print_msg(server, f"§c[-] Extraction failed§r {error}")

def upload_to_firebase(server: PluginServerInterface): #It uploads the zip file to Firebase Storage
    print_msg(server, f"§a[+]§r Uploading to Firebase {conf.fb_path}§r")
    try:
        firebase = pyrebase.initialize_app(conf.firebase_config)
        storage = firebase.storage()
        file = out_path +"."+ conf.extension
        cloudfilename = (conf.fb_path + conf.comp_name +"."+ conf.extension)
        storage.child(cloudfilename).put(file)
        os.remove(file)
        print_msg(server, "§a[+]§r Success")
    except Exception as error:
        print_msg(server, f"§c[-] Uploading failed§r {error}")

def download_from_firebase(server: PluginServerInterface): #It downloads the zip file from Firebase Storage
    print_msg(server, f"§a[+]§r Downloading from Firebase {conf.fb_path}§r")
    try:
        firebase = pyrebase.initialize_app(conf.firebase_config)
        storage = firebase.storage()
        file = conf.comp_name +"."+ conf.extension
        cloudfilename = (conf.fb_path + conf.comp_name +"."+ conf.extension)
        storage.child(cloudfilename).download(conf.dest_path, conf.dest_path+file)
        print_msg(server, "§a[+]§r Success")
    except Exception as error:
        print_msg(server, f"§c[-] ERROR§r {error}")

@new_thread("QBTF Upload")
def upload(server: PluginServerInterface):
    compress_qb(server)
    upload_to_firebase(server)

@new_thread("QBTF Download")
def download(server: PluginServerInterface):
    download_from_firebase(server)
    extract_qb(server)

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
                get_literal_node('upload').runs(lambda src, ctx: upload(src.get_server()))
                ).
            then(
                get_literal_node('download').runs(lambda src, ctx: download(src.get_server()))
            )
    )

def on_load(server: PluginServerInterface, old_module):
    global conf #do conf global
    check_folder(server) #check folder
    conf = server.load_config_simple('config.json', target_class=Configure) #load config.json file to conf
    msg = 'Plugin qbtf loaded, use {}'.format(conf.prefix) #message showed when server start
    server.logger.info(msg) #displays message
    register_command(server) #register command
    server.register_help_message(conf.prefix, {'en_us': help_message}) # when !!help it shows help message
