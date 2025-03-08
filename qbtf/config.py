from mcdreforged.api.utils.serializer import Serializable

# `Configure` is a class that contains the configuration for the `qb_multi` program
class Configure(Serializable):
    prefix: str = '!!qbtf'
    source_path: str = './qb_multi/slot1'
    dest_path: str = './qbtf/'
    firebase_config: dict = {"databaseURL": ""}
    permission: int = 0
    comp_name: str = 'qb_comp'
    extension: str = 'zip'
    fb_path: str = 'smp/'
