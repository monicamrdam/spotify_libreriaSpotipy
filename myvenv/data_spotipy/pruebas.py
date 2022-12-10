import spotipy
from config import Config
from spotipy.oauth2 import SpotifyClientCredentials


clientID = Config.clientID
clientSecret = Config.clientSecret



client_credential_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

estopa = 'spotify:artist:5ZqnEfVdEGmoPxtELhN7ai'



#Obtener datos sobre las canciones TOP del artista
results = sp.artist_top_tracks(estopa)
results.keys()
response = results['tracks']
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()

