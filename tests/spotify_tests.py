# !/usr/bin/env python3  Line 1
# -*- coding: Windows-1252 -*- Line 2
# Imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_locators
import datetime


print(f'Tests started...{datetime.datetime.now()}\n--------------------~*~--------------------\nAuthentication test')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(spotify_locators.client_id, spotify_locators.client_secret))