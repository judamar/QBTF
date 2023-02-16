from mcdreforged.api.utils.serializer import Serializable
from mcdreforged.api.all import ServerInterface


# `Configure` is a class that contains the configuration for the `qb_multi` program
class Configure(Serializable):
    command: str = '!!qbtf'
    source_path: str = './qb_multi/slot1'
    firebase_config: dict = {"databaseURL": ""}
    permission: int = 0
    comp_name: str = 'qb_comp'
    fb_path: str = 'smp/'


# Getting the server interface for the plugin.
psi = ServerInterface.get_instance().as_plugin_server_interface()

# Defining a variable called `help_message` and assigning it the value of the string
# "Use !!qbtf to upload Slot1 to firebase."
help_message = "Use !!qbtf to upload Slot1 to firebase."