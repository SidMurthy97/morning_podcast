import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.getenv("MORNING_PODCAST_CLIENT_ID")
CLIENT_SECRET = os.getenv("MORNING_PODCAST_CLIENT_SECRET")
CLIENT_URI = os.getenv("MORNING_PODCAST_REDIRECT_URI")
SCOPE = 'playlist-modify-private playlist-modify-public'


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_URI,
        scope=SCOPE))


sp.user_playlist_create('1184475550', "test")