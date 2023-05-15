# Quick Backup to Firebase (qbtf)

Requiere `>= v2.0.0a1` [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

Tambien: 
```
pip install pycryptodome
pip install pyrebase4
```

Si al iniciar el server sale un error como este `ImportError: cannot import name 'gaecontrib' from 'requests_toolbelt._compat'`, se soluciona instalando una version anterior al requests-toolbelt con el siguiente comando:
```
pip install requests-toolbelt==0.10.1
```

Este plugin toma el backup del `slot 1` hecho por el [QuickBackupM](https://github.com/TISUnion/QuickBackupM), lo comprime en formato `.zip` y lo sube al storage de firebase.

## Configurar el archivo config.json
```
{
    "command": "!!qbtf",
    "source_path": "./qb_multi/slot1",
    "firebase_config": {
        "databaseURL": ""
    },
    "permission": 0,
    "comp_name": "qb_comp",
    "fb_path": "smp/"
}
```
- El `command` lo puedes modificar por el comando que quieras por si da problemas con el comando de otro plugin o por comodidad.

- El `source_path` ya toma por defecto la ruta del slot1 dentro de los archivos del server.

- En `firebase_config` pones la "key" que sale en el storage de la app en firebase, puedes usar este [tutorial](https://github.com/judamar/QBTF/blob/main/key_tuto.md) para guiarte.

- El `comp_name` es el nombre que va a tener el archivo comprimido tanto en el server como en firebase. No debe tener ninguna extensión.

- El `fb_path` es la ruta que va a tener el archivo dentro de firebase storage, por defecto viene `smp/` pero puedes poner el que sea siempre y cuando termine en `/`.

