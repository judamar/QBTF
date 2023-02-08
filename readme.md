# Quick Backup to Firebase (qbtf)

Este plugin toma el backup del `slot 1` hecho por el [QuickBackupM](https://github.com/TISUnion/QuickBackupM) y lo sube al storage de firebase

## Configurar el archivo config.json
```
{
    "command": "!!qbtf",
    "source_path": "/home/judamar/Escritorio/Mirror/qb_multi/slot1",
    "firebaseConfig": {
        "databaseURL": ""
    }
}
```