import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint
import random
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
CLIENT_URI = os.getenv('CLIENT_URI')
SCOPE = os.getenv('SCOPE')

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
    'spotify:show:51MrXc7hJQBE2WJf2g4aWN' #WSJ briefing 
    'spotify:show:3sVMOI29n5oyMgbUxFz0p3', #more or less 
    'spotify:show:1410RabA4XOqO6IV8p0gYF', #FT news briefing 
    'spotify:show:0hKmFWuxDIlm5IhVICVqWA', #sensemaker 
    'spotify:show:1wr9Zby7ON9HUPoIyTcVEG', #Guardian science weekly 
    'spotify:show:6BXzjkwKxPNAmzVYNZvBTu', #talkSport
    'spotify:show:5zDCsEAvMp61OZOt0CaPS8', #economist news briefing
    'spotify:show:4cnNmAcLfid4aAvvWDnS94' #daily lowdown
]

#get tracks and update playlist

for uri in compulsary_show_uris:
    latest_episode = sp.show_episodes(uri,limit=1)
    latest_episode_uri.append(latest_episode['items'][0]['uri'])

print(latest_episode_uri)

#TODO: assign priority and iterate through played playlists. Maybe hold a dictionary?

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
