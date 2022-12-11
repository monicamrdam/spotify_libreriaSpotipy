import spotipy
from config import Config
from spotipy.oauth2 import SpotifyClientCredentials
from data_spotipy.spotify_client import Artist


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



def album(urn):
    urn = 'spotify:album:5yTx83u3qerZF7GRJu7eFk'
    results = conect().album(urn)
    for i in range(len(results['tracks']['items'])):
        print(results['tracks']['items'][i]['name'])



def artist(urn):
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
    results = conect().artist(urn)
    for i in range(len(results['tracks']['items'])):
        print(results['tracks']['items'][i]['name'])

    #Usando la clase cantnate
    cantante= Artist(results['name'], results ['popularity'], results['uri'])
    cantanteEStopa={
    'name':cantante.name,
    'popularity':cantante.popularity,
    'uri':cantante.uri
    }
    print(cantanteEStopa)


def artist_albums(birdy_uri):
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    results = conect().artist_album(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = conect().next(results)
        albums.extend(results['items'])

    for album in albums:
        print((album['name']))




def artist_related_artists(uri):
    artist_name = 'weezer'
    result = conect().search(q='artist:' + artist_name, type='artist')
    try:
        name = result['artists']['items'][0]['name']
        uri = result['artists']['items'][0]['uri']

        related = sp.artist_related_artists(uri)
        print('Related artists for', name)
        for artist in related['artists']:
            print('  ', artist['name'])
    except BaseException:
        print("usage show_related.py [artist-name]")

def artist_top_tracks(uri):
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
    results = conect().artist_top_tracks(lz_uri)
    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])



def recommendation():
    recommendations = conect().recommendations(seed_genres=['jazz'], limit=1)
    for i in recommendations["tracks"][0]["artists"]:
        print(i["name"])


recommendation()
def track(urn):
    urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'
    results = conect().track(urn)
    for track in results['tracks']:
        print(track['name'] + ' - ' + track['artists'][0]['name'])




def search_artist(artist_name):
    results = conect().search(q='artist:' + artist_name, type='artist',limit=10)
    results['artists']['items']
    longArtist = len(results['artists']['items'])
    print(longArtist)
    for lg in range(longArtist):
        resultado = (results['artists']['items'][lg])['name']
        if resultado.upper() == "ESTOPA":
            print("nombre del artista: " + resultado.lower())







def search_tracks_artist(artist_name):
    results = conect().search(q=artist_name, limit=20)
    results['tracks']['items']
    for i in range(len(results['tracks']['items'])):
        results['tracks']['items'][i]['name']


def search_find_songs_that_start_with_word(word):
    results = conect().search(q=word, type='track', limit=50, offset=0)
    for i in range(len(results['tracks']['items'])):
        results['tracks']['items'][i]['name']
        print ( results['tracks']['items'][i]['name'])


def playlist(playlist_id):
    playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbJiZcmkrIHGU'
    results = conect().playlist(playlist_id)
    print(json.dumps(results, indent=4))



def playlist_items():
    pl_id = 'spotify:playlist:5RIbzhG2QqdkaP24iXLnZX'
    offset = 0

    while True:
        response = sp.playlist_items(pl_id,
                                     offset=offset,
                                     fields='items.track.id,total',
                                     additional_types=['track'])

        if len(response['items']) == 0:
            break

        pprint(response['items'])
        offset = offset + len(response['items'])
        print(offset, "/", response['total'])


def playlist_uriUser():
    playlists = conect().user_playlists('31leeqphiernvfw2rieoy6fbrawy')
    playlists.keys()
    for playlist in playlists['items']:
        playlist['name']
        playlist['uri']
    return



def data_uriUser ():
    data_user = conect().user('31leeqphiernvfw2rieoy6fbrawy')
    data_user.keys()



response_pruebas=''


