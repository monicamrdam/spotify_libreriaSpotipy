import spotipy
from config import Config
from spotipy.oauth2 import SpotifyClientCredentials
from data_spotipy.spotify_client import Artist

clientID = Config.clientID
clientSecret = Config.clientSecret


client_credential_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

estopa = 'spotify:artist:5ZqnEfVdEGmoPxtELhN7ai'

#Obtener datos de un artista
results = sp.artist(estopa)
print (sp.artist(estopa))
results.keys()
cantante= Artist(results['name'], results ['popularity'], results['uri'])


cantanteEStopa={
    'name':cantante.name,
    'popularity':cantante.popularity,
    'uri':cantante.uri
}



response_pruebas=cantanteEStopa
