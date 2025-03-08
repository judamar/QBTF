[English](readme.md) | Español

# Quick Backup to Firebase (qbtf)

[![Descargas en Github](https://img.shields.io/github/downloads/judamar/QBTF/total?label=Descargas%20en%20Github&logo=github)](https://github.com/judamar/QBTF/releases)

Este es un complemento para [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) que permite subir la copia de seguridad realizada por [QuickBackupM](https://github.com/TISUnion/QuickBackupM) a [Firebase](https://firebase.google.com/) Storage.

Requiere `>= v2.0.0a1` de [MCDReforged](https://github.com/Fallen-Breath/MCDReforged).

## Descripción

El complemento QBTF es una herramienta para subir y descargar la copia de seguridad (Slot1 por defecto) a [Firebase](https://firebase.google.com/) Storage.

## Comandos

El complemento QBTF añade los siguientes comandos:
- `!!qbtf`: Muestra el mensaje de ayuda.
- `!!qbtf upload`: Comprime la carpeta Slot1 (por defecto) y la sube a Firebase Storage.
- `!!qbtf download`: Descarga la copia de seguridad desde Firebase Storage y la extrae en Slot1 (por defecto).

## Requisitos
Instala lo siguiente:
```
pip install requests-toolbelt==0.10.1
pip install pycryptodome
pip install pyrebase4
```

## Configuración

Puedes configurar el comportamiento del complemento en el archivo `config.json` con las siguientes opciones:

- **prefix**: Define el prefijo para los comandos del complemento.
- **source_path**: Ruta de la carpeta que se comprimirá y subirá.
- **dest_path**: Ruta donde se almacenarán las copias de seguridad descargadas.
- **firebase_config**: Clave proporcionada por Firebase App Storage, sigue este [tutorial](./tutorials/key_tuto-es.md).
- **permission**: Nivel mínimo de permiso requerido para ejecutar los comandos.
- **comp_name**: Nombre del archivo comprimido.
- **extension**: Extensión del archivo de copia de seguridad.
- **fb_path**: Ruta dentro de Firebase Storage donde se almacenan los archivos.

El complemento debería funcionar sin modificaciones adicionales, siempre que la configuración de Firebase sea correcta.

### Configuración por defecto:

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
