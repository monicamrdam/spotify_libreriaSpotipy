from flask import Flask
from flask import jsonify
from config import Config
from data_spotipy.spotify_service import response
from data_spotipy.pruebas import response_pruebas


app = Flask(__name__)

app.config.from_object(Config)

#Creamos una ruta de prueba home para testear que el servidor funciona
@app.route('/')
def home():
    message={
        "Home":'http://127.0.0.1:3000/',
        'Estopa':'http://127.0.0.1:3000/estopa'
    }
    return jsonify(message)


@app.route ('/estopa')
def estopa():
    #return jsonify(response.json())
    return response

@app.route ('/pruebas')
def estopa_pruebas():
    #return jsonify(response.json())
    return response_pruebas

