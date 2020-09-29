from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv

app = Flask(__name__)

#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#bcrypt = Bcrypt(app)
user = getenv('USERNAME')
password = getenv('PASSWORD')
ip = getenv('IP')
database = getenv('DATABASE')
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + user + ':' + password + '@' + ip + '/' + database
#db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
SPOTIPY_CLIENT_ID = getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = getenv('redirect')
from application import routes
