from flask import Flask

app = Flask(__name__) # Esto crea una instancia de la clase Flask. __name__ es el nombre del módulo de la aplicación.

from app import routes # Importar el módulo de routes, que define el comportamiento de la API.
