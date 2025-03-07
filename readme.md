English | [Español](readme-es.md)

# Quick Backup to Firebase (qbtf)

[![Github downloads](https://img.shields.io/github/downloads/judamar/QBTF/total?label=Github%20downloads&logo=github)](https://github.com/judamar/QBTF/releases)

This is a plugin for [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) that allows upload the backup made by [QuickBackupM](https://github.com/TISUnion/QuickBackupM) to the [Firebase](https://firebase.google.com/) Storage.

Requires `>= v2.0.0a1` [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

## Description

The QBTF plugin is a tool for upload and download the backup (Slot1 by default) to the [Firebase](https://firebase.google.com/) Storage.

## Commands

The QBTF plugin adds the following commands:
- `!!qbtf`: Displays help message.
- `!!qbtf upload`: Compresses the Slot1 (by default) folder and uploads it to Firebase Storage.
- `!!qbtf download`: Downloads the backup from Firebase Storage and extracts it into Slot1 (by default).

## Requirements
Install this:
```
pip install requests-toolbelt==0.10.1
pip install pycryptodome
pip install pyrebase4
```


## Configuration

You can configure the plugin's behavior in the `config.json` file with the following options:

- **prefix**: Defines the prefix for the plugin's commands.
- **source_path**: Path of the folder to be compressed and uploaded.
- **dest_path**: Path where the downloaded backups will be stored.
- **firebase_config**: Key provided by Firebase App Storage, follow this [tutorial](https://github.com/judamar/QBTF/blob/main/tutorials/key_tuto.md).
- **permission**: Minimum permission level required to execute commands.
- **comp_name**: Name of the compressed file.
- **extension**: Backup file extension.
- **fb_path**: Path within Firebase Storage where files are stored.

The plugin should work without additional modifications, as long as the Firebase configuration is correct.

### Default Configuration:

```json
{
    "prefix": "!!qbtf",
    "source_path": "./qb_multi/slot1",
    "dest_path": "./qbtf/",
    "firebase_config": {"databaseURL": ""},
    "permission": 0,
    "comp_name": "qb_comp",
    "extension": "zip",
    "fb_path": "smp/"
}

- En `firebase_config` pones la "key" que sale en el storage de la app en firebase, puedes usar este  para guiarte.

