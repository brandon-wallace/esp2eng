from flask import Blueprint
auth = Blueprint('auth', __name__)

from application.auth import routes
