from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from application.main import main


@main.route('/')
def index():
    '''Index route'''

    return render_template('main/index.html')


@main.app_errorhandler(404)
def page_not_found(error):
    '''404 Page not found'''

    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(error):
    '''505 Internal server error'''

    return render_template('500.html'), 500
