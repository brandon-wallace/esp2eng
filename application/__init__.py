import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_debugtoolbar import DebugToolbarExtension
import requests
from bs4 import BeautifulSoup


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
# toolbar = DebugToolbarExtension()


def create_app():
    '''Create application'''

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # toolbar.init_app(app)

    from application.main.routes import main
    app.register_blueprint(main)

    from application.auth.routes import auth
    app.register_blueprint(auth)

    return app


def scraper():
    '''Scrap word of the day'''

    response = requests.get("https://www.spanishdict.com/wordoftheday")
    html = BeautifulSoup(response.content, 'html.parser')
    sentences = html.find_all("div", attrs={'class': 'sd-wotd-example-source'})
    data = {}

    for sentence in sentences:
        s = sentence.string
        data[s] = sentence.attrs['class']
        print(data[s])
    return
