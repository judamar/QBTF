from mcdreforged.api.all import *
import pyrebase
import shutil
from src.config import Configure

config = Configure


def comprimir_qb(server: PluginServerInterface): 
    """
    It compresses the source code of the plugin into a zip file.
    
    :param server: PluginServerInterface
    :type server: PluginServerInterface
    """
    global config
    config = server.load_config_simple('config.json', target_class=Configure)
    server.say("§3Comprimiendo...§r")
    try:
        shutil.make_archive('qb_comp', 'zip', config.source_path)
        server.say("§a[+]§r DONE")
    except:
        server.say("§c[-]§r Algo falló")

def subirAFirebase(server: PluginServerInterface):
    """
    It uploads a file to Firebase
    
    :param server: PluginServerInterface
    :type server: PluginServerInterface
    """
    global conf
    conf = server.load_config_simple('config.json', target_class=Configure)
    firebase = pyrebase.initialize_app(conf.firebaseConfig)
    storage = firebase.storage()
    server.say("§3Subiendo a Firebase...§r")
    try:
        file = "qb_comp.zip"
        cloudfilename = "qb/qb_comp.zip" 
        storage.child(cloudfilename).put(file)
        server.say("§a[+]§r DONE")
    except:
        server.say("§c[-]§r Algo falló")
