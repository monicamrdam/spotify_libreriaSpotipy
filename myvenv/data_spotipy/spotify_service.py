import spotipy
from config import Config
from spotipy.oauth2 import SpotifyClientCredentials
from data_spotipy.spotify_client import Artist, Top_Tracks

def clienId():
    clientID = Config.clientID
    return clientID
def clientSecret():
    clientSecret = Config.clientSecret
    return clientSecret
def conect():
    client_credential_manager = SpotifyClientCredentials(client_id=clienId(), client_secret=clientSecret())
    sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)
    return sp


def uri_artist():
    estopa = 'spotify:artist:5ZqnEfVdEGmoPxtELhN7ai'
    return estopa



def artist(urn):
    gemderList=[]
    results = conect().artist(urn)
    for genres in results['genres']:
        gemderList.append(genres)
    estopa_datos=Artist(results['name'], results['popularity'], results['uri'], gemderList)
    Estopa={
        'name': estopa_datos.name,
        'popularity': estopa_datos.popularity,
        'uri': estopa_datos.uri,
        'gender':estopa_datos.gender
    }
    return Estopa


def artist_top_tracks(uri):
    allTracks=[]
    results = conect().artist_top_tracks(uri)
    for track in results['tracks'][:5]:
        tracks_Datos= Top_Tracks(track['name'], track['popularity'], track['preview_url'])
        Estopa_Track={
            'name': tracks_Datos.name,
            'popularity': tracks_Datos.popularity,
            'audioSong': tracks_Datos.audioSong,
        }
        allTracks.append(Estopa_Track)
    return allTracks


def mostrar_todosdatos():
    todosdatos={
        'informacion artista':artist(uri_artist()),
        'informacion top track': artist_top_tracks(uri_artist())
    }
    return  todosdatos


response=mostrar_todosdatos()

