import os
from dotenv import load_dotenv

#Cargamos las variables de entorno en memoria
load_dotenv()

#Clase para definir la configuración de la aplicación
class Config():
    SERVER_NAME= '127.0.0.1:3000'
    DEBUG= True

    clientID= os.environ.get('SPOTIPY_CLIENT_ID', '')
    clientSecret= os.environ.get('SPOTIPY_CLIENT_SECRET','')




