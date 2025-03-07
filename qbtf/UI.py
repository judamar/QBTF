from mcdreforged.api.rtext import RTextList, RText, RColor
from qbtf.config import Configure

conf = Configure()
prefix = conf.prefix

help_head = """
==================§b QBTF §r==================
"""
help_body = {
    f"§b{prefix}": "§rDisplay help message.",
    f"§b{prefix} upload": "§rUpload the Slot1 to Firebase storage.",
    f"§b{prefix} download": "§rDownload the file and extract in Slot1."
}

def gen_help_message():
    help_message = RTextList(
        RText(help_head),
        RText("Available Commands:", color=RColor.gold),
    )
    for command, description in help_body.items():
        help_message.append(f"\n  {command} - {description}")
    return help_message

def gen_unknown_argument_message():
    unknown_message = RText("Unknown argument.", color=RColor.red)
    return str(unknown_message)