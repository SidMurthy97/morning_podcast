import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint
CLIENT_ID = os.getenv("MORNING_PODCAST_CLIENT_ID")
CLIENT_SECRET = os.getenv("MORNING_PODCAST_CLIENT_SECRET")
CLIENT_URI = os.getenv("MORNING_PODCAST_REDIRECT_URI")
SCOPE = 'playlist-modify-private playlist-modify-public'

usernames = ['1184475550']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_URI,
        scope=SCOPE))

playlist_uri = 'spotify:playlist:49bH2WkTveKn9JYAjBNyfJ'

show_uris = [
    'spotify:show:2qZ0xpaBBwf3bTYhA10KZY', #daily briefing  
    'spotify:show:29eeC2kUEpYkDIYO4Bj0Qr', #tech briefing
    'spotify:show:1VXcH8QHkjRcTCEd88U3ti', #ted talks daily
    'spotify:show:0hKmFWuxDIlm5IhVICVqWA'
    ] 


latest_episode_uri = [] #store list of all uris
for uri in show_uris:
    latest_episode = sp.show_episodes(uri,limit=1)
    latest_episode_uri.append(latest_episode['items'][0]['uri'])


sp.playlist_replace_items(playlist_uri, latest_episode_uri)
