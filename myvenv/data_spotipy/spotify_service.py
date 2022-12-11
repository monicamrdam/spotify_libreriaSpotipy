import spotipy
from config import Config
from spotipy.oauth2 import SpotifyClientCredentials


clientID = Config.clientID
clientSecret = Config.clientSecret



client_credential_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

estopa = 'spotify:artist:5ZqnEfVdEGmoPxtELhN7ai'


response =''

