from application.models import User
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import (InputRequired, Email, EqualTo,
                                Length, ValidationError)


class SignUpForm(FlaskForm):
    '''Sign up form for new users'''

    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(),
                             Length(min=4, max=32)])
    confirm_password = PasswordField('Re-Enter Password', validators=[
                                     InputRequired(), EqualTo('password')])
    submit = SubmitField('SIGN UP')

    def validate_email(self, email):
        '''Check for existing email'''
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists.')

    def validate_username(self, username):
        '''Check for existing username'''

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')


class LoginForm(FlaskForm):
    '''Login form for registered users'''

    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('LOGIN')


class AddEntryForm(FlaskForm):
    '''Add entry form'''

    word_es = StringField('Add Spanish Vocabulary Word',
                          validators=[InputRequired()])
    sentence1_es = StringField('Spanish Example Sentence 1',
                               validators=[InputRequired()])
    sentence1_en = StringField('English Translation',
                               validators=[InputRequired()])
    sentence2_es = StringField('Spanish Example Sentence 2',
                               validators=[InputRequired()])
    sentence2_en = StringField('English Translation',
                               validators=[InputRequired()])
    sentence3_es = StringField('Spanish Example Sentence 3')
    sentence3_en = StringField('English Translation')
    definition1_en = StringField('English Definition 1',
                                 validators=[InputRequired()])
    definition2_en = StringField('English Definition 2')
    definition3_en = StringField('English Definition 3')
    definition4_en = StringField('English Definition 4')
    submit = SubmitField('ADD ENTRY')
