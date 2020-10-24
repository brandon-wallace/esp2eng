from application.models import User
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import (InputRequired, Email, EqualTo,
                                Length, ValidationError)


class SignUpForm(FlaskForm):
    '''Sign up form for new users'''

    username = StringField('Username', validators=[InputRequired()])
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
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
        return


class LoginForm(FlaskForm):
    '''Login form for registered users'''

    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('LOGIN')
