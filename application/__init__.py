import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
# from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
# toolbar = DebugToolbarExtension()


def create_app():
    '''Create application'''

    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAACRIxA7wvXjIE411PfdB2gt2J'
    # app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeYIbsSAAAJezFt_hSTo0YtyeFG-Jgtu'

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    # toolbar.init_app(app)

    from application.main.routes import main
    app.register_blueprint(main)

    from application.auth.routes import auth
    app.register_blueprint(auth)

    return app
