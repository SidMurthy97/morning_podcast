import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint
import random

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

latest_episode_uri = [] #store list of all uris
optional_episode_uri = [] #store list of all uris

#first include some tech briefings you defo want
compulsary_show_uris = [
    'spotify:show:2qZ0xpaBBwf3bTYhA10KZY', #daily briefing  
    'spotify:show:29eeC2kUEpYkDIYO4Bj0Qr', #tech briefing
    ] 

#optional shows in a random order
optional_show_uris = [
    'spotify:show:3sVMOI29n5oyMgbUxFz0p3', #more or less 
    'spotify:show:1410RabA4XOqO6IV8p0gYF', #FT news briefing 
    'spotify:show:0hKmFWuxDIlm5IhVICVqWA' #sensemaker 
]

#get tracks and update playlist

for uri in compulsary_show_uris:
    latest_episode = sp.show_episodes(uri,limit=1)
    latest_episode_uri.append(latest_episode['items'][0]['uri'])

print(latest_episode_uri)

for uri in optional_show_uris:
    latest_episode = sp.show_episodes(uri,limit=1)

    #get episode duration in minutes
    episode_duration = (latest_episode['items'][0]['duration_ms']) / (1000 * 60) 
    
    if episode_duration > 15:
        break
    
    optional_episode_uri.append(latest_episode['items'][0]['uri'])

random.shuffle(optional_episode_uri)
latest_episode_uri += optional_episode_uri
print(latest_episode_uri)

sp.playlist_replace_items(playlist_uri, latest_episode_uri)
