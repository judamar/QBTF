from mcdreforged.api.all import *
from src import my_lib
from src.config import Configure

conf = Configure

def on_load(server: PluginServerInterface, old_module):
	"""
	It loads the configuration file and prints a message to the console
	
	:param server: PluginServerInterface
	:type server: PluginServerInterface
	:param old_module: The old module object, if the plugin is reloaded
	"""
	global conf
	conf = server.load_config_simple('config.json', target_class=Configure)
	msg = 'Plugin qbtf loaded, use {}'.format(conf.command)
	server.logger.info(msg)


def on_user_info(server: PluginServerInterface, info: Info):
	"""
	It uploads the slot 1 to firebase.
	
	:param server: PluginServerInterface
	:type server: PluginServerInterface
	:param info: This is the info object that contains the message that was sent
	:type info: Info
	"""
	if info.content == conf.command:
		my_lib.comprimir_qb(server)
		my_lib.subirAFirebase(server)
		server.logger.info("§a[+]§r Slot 1 uploaded to firebase!")
