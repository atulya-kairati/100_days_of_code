import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# The Playlists are create in beanmd2 Id(login through fb) and credentials belong to same id

client_info = {
    "client_secret": "821721615b6e412c97e6e42ce417fceb", "client_id": "86b50d51d827481d887b092c1b1b5b6f",
}


def get_song_from_span(span_tag):
    return span_tag.find(
        class_="chart-element__information__song text--truncate color--primary").getText()  # it has 3 classes


def get_artist_from_span(span_tag):
    return span_tag.find(class_="chart-element__information__artist").getText()


def get_spotify_uris(on_date: str):
    songs = get_top100_at_date(on_date=on_date)
    year = on_date.split('-')[0]
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(**client_info))

    spotify_uris = []
    for song, artist in songs:
        search = sp.search(f"track:{song}  year:{year}", type="track", limit=1)
        try:
            spotify_uris.append(search['tracks']['items'][0]['uri'])
        except IndexError:
            print(f"Spotify song for {song} by {artist} not found")

    return spotify_uris


def get_top100_at_date(on_date: str):
    res = requests.get(f"https://www.billboard.com/charts/hot-100/{on_date}")
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    all_span_tags = soup.find_all(name="span", class_="chart-element__information")

    return [(get_song_from_span(span), get_artist_from_span(span)) for span in all_span_tags]


def create_playlist(name, uris: list):
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            redirect_uri="http://localhost/",
            show_dialog=True,
            cache_path="token.txt", **client_info,
        )
    )

    user_id = sp.current_user()["id"]

    playlist = sp.user_playlist_create(name=name, user=user_id, public=False)
    print(playlist)
    sp.playlist_add_items(playlist_id=playlist['id'], items=uris)


date = input("Enter Date (yyyy-mm-dd): ")
create_playlist(f'{date} Hits', uris=get_spotify_uris(on_date=date))
