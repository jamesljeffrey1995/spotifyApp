from application import app, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from flask import render_template, redirect, url_for, request, Flask, jsonify, redirect
from flask_login import login_user, current_user, logout_user, login_required, current_user
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tekore as tk



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    return render_template("home.html")
