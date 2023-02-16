import shutil
import pyrebase
from mcdreforged.api.all import *
from qbtf.config import *

conf = Configure

def comprimir_qb(server: PluginServerInterface): #It compresses the source code of the plugin into a zip file.
	psi.logger.info("§3Compressing...§r")
	try:
		shutil.make_archive(conf.comp_name, 'zip', conf.source_path)
		psi.logger.info("§a[+]§r DONE")
	except:
		psi.logger.info("§c[-]§r Epic fail")

def subirAFirebase(server: PluginServerInterface): #It uploads the zip file to Firebase Storage
    firebase = pyrebase.initialize_app(conf.firebase_config)
    storage = firebase.storage()
    psi.logger.info("§3Uploading to Firebase...§r")
    try:
        file = conf.comp_name + '.zip'
        cloudfilename = (conf.fb_path + file)
        storage.child(cloudfilename).put(file)
        psi.logger.info("§a[+]§r DONE")
    except:
        psi.logger.info("§c[-]§r Epic fail")

def execute(server: PluginServerInterface): #Executes 'comprimir_qb' and 'subirAFirebase' functions
	comprimir_qb(server)
	subirAFirebase(server)

def on_load(server: PluginServerInterface, old_module):
	global conf #do conf global
	conf = server.load_config_simple('config.json', target_class=Configure) #load config.json file to conf
	msg = 'Plugin qbtf loaded, use {}'.format(conf.command) #message showed when server start
	server.logger.info(msg) #displays message
	server.register_command(Literal(conf.command).runs(execute)) #execute plugin
	server.register_help_message(conf.command, {'en_us': help_message}) # when !!help it shows help message
