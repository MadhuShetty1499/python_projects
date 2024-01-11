import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_USER_NAME = os.environ.get("SPOTIFY_USER_NAME")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")
songs = soup.select("li ul li h3")
songs_list = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        cache_path="token.txt",
        show_dialog=True,
        username=SPOTIFY_USER_NAME,
    )
)
user_id = sp.current_user()['id']

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, public=False, name=playlist_name)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
