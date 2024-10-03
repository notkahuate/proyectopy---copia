import os
import json

MY_DATABASE = 'data/liga.json'  

def NewFile(data):
    """Crea un nuevo archivo JSON y guarda los datos."""
    with open(MY_DATABASE, "w") as wf:
        json.dump(data, wf, indent=4)

def ReadFile():
    """Lee el contenido del archivo JSON y lo devuelve como un diccionario."""
    if os.path.isfile(MY_DATABASE):
        with open(MY_DATABASE, "r") as rf:
            return json.load(rf)
    else:
        return {}

def CheckFile(initial_data):
    """Verifica si el archivo existe; si no, lo crea."""
    if not os.path.isfile(MY_DATABASE):
        NewFile(initial_data)
