[English](key_tuto.md) | Español

# Tutorial

1. Abre [firebase](https://console.firebase.google.com/u/0/), inicia sesion con Google y haz click en `Agregar proyecto`.
2. Ponle un nombre al proyecto, dale `Continuar`, el paso 2 tambien `Continuar`, en el paso 3 seleccionas la que dice `Default account to firebase` y le das a `Crear proyecto`.
3. Abres tu proyecto y en el panel derecho buscas `Storage`, y abres dicha opción.
4. Le das a `empezar`, `siguiente`, y `hecho`. 
5. Cuando lo tengas creado, en la parte de arriba te saldrá algo como esto. Le das donde dice `Rules`.

[![st-rules.png](https://i.postimg.cc/3r9Rp1qc/st-rules.png)](https://postimg.cc/w3ygYXgX)

6. En el apartado Editar Reglas, cambias el `allow read, write: if request.auth != null;` por `allow read, write: if true;` y le das en `Pubicar`.

[![allow-true.png](https://i.postimg.cc/VLpzBVWD/allow-true.png)](https://postimg.cc/qzcfpQY3)

7. Vuelves al overview de tu proyecto y le das al </> WEB, registras la app sin darle check a nada. Te saldrá un archivo de configuración.

[![overview.png](https://i.postimg.cc/9Xk6vqwf/overview.png)](https://postimg.cc/w3h4NMVK)

8. Copias el contenido de la variable firebaseConfig y lo pegas en la misma variable dentro del archivo de configuración del plugin pero como si fuera [diccionario](https://youtube.com/clip/Ugkxc8d-DNlt49jpA5VZ0sw9pmpYBv2ZX1xx) es decir, llave y contenido dentro de "" dejando la ultima llave ("databaseURL": "") y le das Continuar a la consola.

[![key.png](https://i.postimg.cc/76jyMCgb/key.png)](https://postimg.cc/G8PNbmg1)

Ya podrías correr el plugin de forma correcta.
