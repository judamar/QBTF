from mcdreforged.api.utils.serializer import Serializable

# `Configure` is a class that has a `command` attribute that is a string, a `source_path` attribute
# that is a string, and a `firebaseConfig` attribute that is a dictionary
class Configure(Serializable):
    command: str = '!!qbtf'
    source_path: str = '/foo/bar/qb_multi/slot1'
    firebaseConfig: dict = {"databaseURL": ""}
