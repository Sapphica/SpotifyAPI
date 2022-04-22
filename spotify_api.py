# !/usr/bin/env python3  Line 1
# -*- coding: Windows-1252 -*- Line 2
# Imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_locators

artist = 'Nirvana'
# artist = input('Search for Artist: ')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(spotify_locators.client_id, spotify_locators.client_secret))
print(f'Listed Albums for {artist}')
results = spotify.artist_albums(spotify_locators.search_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


