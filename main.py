import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint
CLIENT_ID = os.getenv("MORNING_PODCAST_CLIENT_ID")
CLIENT_SECRET = os.getenv("MORNING_PODCAST_CLIENT_SECRET")
CLIENT_URI = os.getenv("MORNING_PODCAST_REDIRECT_URI")
SCOPE = 'playlist-modify-private playlist-modify-public'

usernames = ['1184475550']

podcasts_to_add = [
    'spotify:episode:3MzCRf8RUWHpnXuKFG19qI'
]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=CLIENT_URI,
        scope=SCOPE))


# for user in usernames: 
#     sp.user_playlist_create(user,"test")
#     created_playlist = sp.user_playlists(user,limit = 1)
#     playlist_id = created_playlist['items'][0]['id']
#     # print(playlist_id)
    

    # sp.playlist_add_items(playlist_id,podcasts_to_add)

'''TODO: decide on list of episodes to add
TODO: write function to update the playlist rather than create it each day
TODO: Abstract episde to show level, such that the most recent episode URI can
be got each morning.'''


playlist_uri = 'spotify:playlist:49bH2WkTveKn9JYAjBNyfJ'
show_uris = ['spotify:show:5CHMS8JT6vz45eRq1cGY0t'] 
latest_episode_uri = [] #store list of all uris
for uri in show_uris:
    latest_episode = sp.show_episodes(uri,limit=1)
    latest_episode_uri.append(latest_episode['items'][0]['uri'])


sp.playlist_add_items(playlist_uri, latest_episode_uri)
