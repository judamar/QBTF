# Quick Backup to Firebase (qbtf)

Requiere `>= v2.0.0a1` [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

Tambien: 
```
pip install pycryptodome
pip install pyrebase4
```

Este plugin toma el backup del `slot 1` hecho por el [QuickBackupM](https://github.com/TISUnion/QuickBackupM) y lo sube al storage de firebase.

## Configurar el archivo config.json
```
{
    "command": "!!qbtf",
    "source_path": "....../qb_multi/slot1",
    "firebase_onfig": {
        "databaseURL": ""
    }
}
```
En `source_path` pones la ruta del slot 1. (**no** debe ternimar en /)
En `firebase_config` pones la "key" que sale en el storage de la app en firebase, puedes usar este [link](https://www.youtube.com/watch?v=zGGq3kBedR8&list=PLs3IFJPw3G9Jwaimh5yTKot1kV5zmzupt&index=2) para guiarte.