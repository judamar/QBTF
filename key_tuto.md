# Tutorial.

1. Abre [firebase](https://console.firebase.google.com/u/0/), inicia sesion con Google y haz click en `Agregar proyecto`.
2. Ponle un nombre al proyecto, dale Continuar, el paso 2 tambien Continuar, en el paso 3 seleccionas la que dice `Default account to firebase` y le das a Crear proyecto.
3. Abres tu proyecto y en el panel derecho buscas `Storage`, y abres dicha opción.
4. Le das a empezar, siguiente, y hecho. 
5. Cuando lo tengas creado, en la parte de arriba te saldrá algo como esto. Le das donde dice Rules.

![snapshot](https://raw.githubusercontent.com/judamar/QBTF/blob/main/ss/st_rules.png)

6. En el apartado Editar Reglas, cambias el `allow read, write: if request.auth != null;` por `allow read, write: if true;` y le das en Pubicar.

![snapshot](https://raw.githubusercontent.com/judamar/QBTF/blob/main/ss/allow_true.png)

7. Vuelves al overview de tu proyecto y le das al `</>` WEB, registras la app sin darle check a nada. Te saldrá un archivo de configuración.

![snapshot](https://raw.githubusercontent.com/judamar/QBTF/blob/main/ss/overview.png)

8. Copias el contenido de la variable `firebaseConfig` y lo pegas en la misma variable dentro del archivo de configuración del plugin pero como si fuera diccionario es decir, llave y contenido dentro de `""` dejando la ultima llave (databaseURL) y le das Continuar a la consola.

![snapshot](https://raw.githubusercontent.com/judamar/QBTF/blob/main/ss/key.png)

Ya podrías correr el plugin de forma correcta.
