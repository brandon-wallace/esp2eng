from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from application import db
from application.main import main
from application.forms import AddEntryForm
from application.models import Word


@main.route('/')
def index():
    '''Index route'''

    return render_template('main/index.html')


@main.route('/add-word', methods=['GET', 'POST'])
@login_required
def add_word():
    '''Add a word to database'''

    form = AddEntryForm()
    if form.validate_on_submit():
        try:
            word = Word(word_es=form.word_es.data,
                        sentence1_es=form.sentence1_es.data,
                        sentence1_en=form.sentence1_en.data,
                        sentence2_es=form.sentence2_es.data,
                        sentence2_en=form.sentence2_en.data,
                        sentence3_es=form.sentence3_es.data,
                        sentence3_en=form.sentence3_en.data,
                        definition1_en=form.definition1_en.data,
                        definition2_en=form.definition2_en.data,
                        definition3_en=form.definition3_en.data,
                        definition4_en=form.definition4_en.data)
            db.session.add(word)
            db.session.commit()
            db.session.remove()
            flash('Word added successfully', 'success')
        except IntegrityError:
            db.session.rollback()
            return redirect(url_for('main.add_word'))
    return render_template('main/add_word.html', form=form)


@main.app_errorhandler(404)
def page_not_found(error):
    '''404 Page not found'''

    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(error):
    '''505 Internal server error'''

    return render_template('500.html'), 500
