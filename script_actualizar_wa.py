import pyautogui as mouse
import time
from os import system
import subprocess
import test as t

# tener en cuenta que el celular debe estar enchufado por usb
# y estar con scrcpy en pantalla completa con el comando scrcpy --fullscreen
# tambien si estas usando windowns debes activar el venv
# lo primero es ir en una terminal con permisos de administrador a la carpeta del proyecto 
# luego ejecutar el comando: python -m venv venv luego de ejecutarlo se creara una carpeta llamada venv 
# y antes de ejecutar el script de python se debe ejecutar .\venv\Script\Activate
# luego de esto ejecutar el script de python con .\script_actualizar_wa.py

def click(boton):
    mouse.mouseDown(button=boton)
    mouse.mouseUp(button=boton)


def mover(x,y):
    mouse.moveTo(x,y)
    time.sleep(1)
    print("hago click")
    click("left")

def actualizar():
    task = subprocess.Popen(cmd, shell=True)
    time.sleep(3)
    print(mouse.position())
    mover(820,700)
    # time.sleep(2)
    mover(822,65)
    # time.sleep(2)
    mover(763,140)
    # time.sleep(2)
    mover(546,68)
    # time.sleep(2)
    click("left")
    time.sleep(3)
    subprocess.Popen("TASKKILL /F /PID {} /T".format(task.pid))
    # mouse.hotkey("altleft","F4")



if __name__ == '__main__':
    actualizar()
