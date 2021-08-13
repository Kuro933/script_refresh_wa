from __future__ import print_function
import time
import flask as flask
import script_actualizar_wa as wa
from flask_restful import Resource, Api
import requests as peticion
import json
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# si necesitas modificar los scopes, borrar el archivo llamado token.json
SCOPES = ['https://www.googleapis.com/auth/contacts',
          'https://www.googleapis.com/auth/contacts.readonly']


def acreditar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('people', 'v1', credentials=creds)
    return service


app = flask.Flask(__name__)
api = Api(app)
service = acreditar()


@app.route('/py/listarContactos')
def listarContactos():
    # service = acreditar()
    grupo = ""
    print('List 10 connection names')
    results = service.people().connections().list(resourceName='people/me',
                                                  personFields='names,phoneNumbers').execute()
    connections = results.get('connections', [])
    for person in connections:
        names = person.get('names', [])
        numero = person.get('phoneNumbers', [])
        if names:
            name = person.get("resourceName")
            grupo = grupo + "\n" + name
    return grupo


@app.route('/py/test', methods=['GET', 'POST'])
def add_message():
    json_data = flask.request.json
    valor = json_data["id"]
    text = json_data["text"]
    print(valor, text)
    return "ok"


@app.route('/py/agregarContacto', methods=['GET', 'POST'])
def agregar():
    # service = acreditar()
    json_data = flask.request.json
    nombre = json_data["nombre"]
    valor = json_data["numero"]
    numero = "+549" + valor
    body = "{\"names\": [{\"givenName\": \"%s\"}],\"phoneNumbers\": [{\"value\": \"%s\"}]}" % (
        numero, numero)
    data = json.loads(body)
    service.people().createContact(body=data).execute()
    time.sleep(4)
    wa.actualizar()
    return "Contacto agregado con exito"


@app.route('/py/contacto')
def contacto():
    respuesta = "no existe"
    json_data = flask.request.json
    nombre = json_data["nombre"]
    numero = json_data["numero"]
    body = "{\"query\": \"%s\", \"readMask\": \"names\"}" % (nombre)
    data = json.loads(body)
    resultado = service.people().searchContacts(query=nombre, readMask="names").execute()
    persona = resultado.get('results',[])

    print("soy nuevo mensaje pa ver si funca pm2")
    if(persona):
        respuesta = "existe"
    return respuesta


@app.route('/py/eliminarContacto', methods=['GET', 'POST'])
def eliminar():
    rn = ""
    json_data = flask.request.json
    nombre = json_data["nombre"]
    body = "{\"query\": \"%s\", \"readMask\": \"names\"}" % (nombre)
    data = json.loads(body)
    resultado = service.people().searchContacts(query=nombre, readMask="names").execute()
    persona = resultado.get('results',[])
    for person in persona:
        rn = person.get('person').get('resourceName')
    result = service.people().deleteContact(resourceName=rn).execute()
    time.sleep(4)
    wa.actualizar()
    return "contacto eliminado"

if __name__ == '__main__':
    app.run(debug=True, port=14000)
