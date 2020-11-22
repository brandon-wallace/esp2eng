# from os import environ
from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as TJWSS
from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    '''Login user to session'''

    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    '''User table'''

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    account_created_on = db.Column(db.DateTime, nullable=False,
                                   default=datetime.utcnow)
    words = db.relationship('Word', backref='author', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Word(db.Model):
    '''Word table'''

    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    word_es = db.Column(db.String(150), unique=True, nullable=False)
    sentence1_es = db.Column(db.String(150), nullable=False)
    sentence1_en = db.Column(db.String(150), nullable=False)
    sentence2_es = db.Column(db.String(150), nullable=True)
    sentence2_en = db.Column(db.String(150), nullable=True)
    sentence3_es = db.Column(db.String(150), nullable=True)
    sentence3_en = db.Column(db.String(150), nullable=True)
    definition1_en = db.Column(db.String(50), nullable=False)
    definition2_en = db.Column(db.String(50), nullable=True)
    definition3_en = db.Column(db.String(50), nullable=True)
    definition4_en = db.Column(db.String(50), nullable=True)
    date_added = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
