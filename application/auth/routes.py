from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from application import db, bcrypt
from application.models import User
from application.forms import SignUpForm, LoginForm

auth = Blueprint('auth', __name__,
                 template_folder='templates',
                 static_folder='static')


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    '''Sign up route'''

    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))

    form = SignUpForm()
    if form.validate_on_submit():
        try:
            hashed_password = bcrypt.generate_password_hash(form.password.data
                                                            ).decode('utf-8')
            user = User(username=form.username.data,
                        firstname=form.firstname.data,
                        lastname=form.lastname.data,
                        email=form.email.data,
                        password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return url_for('auth.login')
        except Exception:
            flash('An error ocurred!', 'danger')
            return redirect(url_for('auth.signup'))
    return render_template('auth/signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Login route'''

    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,
                                                   form.password.data):
                login_user(user)
                # next_page = request.args.get('next')
                # if next_page:
                #     return redirect(next_page)
                flash('Login successful!', 'success')
                return redirect(url_for('auth.profile'))
            else:
                flash('Login unsuccessful. Please check email/password.',
                      'danger')
                return redirect(url_for('auth.login'))
        except Exception as e:
            print(e)
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/profile')
@login_required
def profile():
    '''User profile route'''

    user_initials = current_user.firstname[0] + current_user.lastname[0]
    return render_template('auth/profile.html', user_initials=user_initials)


@auth.route('/logout')
def logout():
    '''Log out route'''

    logout_user()
    flash('You have been logged out.', 'success')
    return render_template('main/index.html')


@auth.route('/terms_of_service')
def terms_of_service():
    '''terms_of_service'''

    return render_template('auth/terms_of_service.html')


@auth.route('/privacy_policy')
def privacy_policy():
    '''privacy_policy'''

    return render_template('auth/privacy_policy.html')
