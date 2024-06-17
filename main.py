import requests

from flask import Flask

app = Flask(__name__)
app.secret_key = 'test1wsazxasmansiabddvasfv423b213b2132323'


CLIENT_ID = 'fb9ba38989444a259af61ce8f69878ac'
CLIENT_SECRET = 'd5a4b236ab6e4d40877817db357e873d'
REDIRECT_URL = 'http://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL =  'https://accounts.spotify.com/token'
API_BASE_URL = 'https://api.spotify.com/v1/'



@app.route('/')
def index():
    return "Welcome to my Spotify App <a> href = '/login'>Login with SPotify</a>"

