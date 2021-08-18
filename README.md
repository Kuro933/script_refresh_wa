# script_refresh_wa

**Pasos para comenzar**
```
1- git clone https://github.com/Kuro933/script_refresh_wa.git
2- abrir una terminal y ejecutar python -m venv venv esto creara una carpeta llamada venv
3- ejecutar el comando .\venv\Script\activate y estaras en el entorno virtual (venv)
4- ejecutar pip install -r requirements.txt
```
de esta forma se instalara todas las librerias y dependencias que se necesitan para que el proyecto funcione

# Correr el proyecto
En una tarminal si no estas ya en el venv realizar lo siguiente
```
1- .\venv\Script\activate
2- python contactos.py
```
si ya estas dentro del venv
```
python contactos.py
```
con el entorno virtual de python ejecutar contactos.py
el proyecto este tiene la funcionalidad de API, interactua con llamadas a sus "@app.route"
de esta forma puede ser utilizado desde distintos tipos de aplicaciones externas


# Importante
Tener en cuenta que para que funcione la API de google, se debe crear en cloud google con una cuenta asociadada a un celular
una API y crear el cliente para que tenga acceso, una vez hecho esto, te dejara bajar las credenciales en un json, el cual
una vez descargado cambiarle el nombre por credentials.json y dejarlo en la carpeta del proyecto
