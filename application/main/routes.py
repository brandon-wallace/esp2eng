from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
# from flask_paginate import Pagination, get_page_parameter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func
from application import db
# from application.main import main
from application.forms import AddEntryForm
from application.models import Word

main = Blueprint('main', __name__,
                 template_folder='templates',
                 static_folder='static')


@main.route('/')
def index():
    '''Index route'''

    # page = request.args.get(get_page_parameter(), 1, type=int)
    # page = request.args.get('page', 1, type=int)
    # words = Word.query.order_by(func.random()).paginate(page, per_page=5)
    words = Word.query.order_by(func.random()).limit(2)
    # words = Word.query.paginate(page=page, per_page=2)
    # words = Word.query.order_by(func.random())
    # pagination = Pagination(page=page, total=words.count(), search=False,
    #                         record_name="Test")
    return render_template('main/index.html', words=words)
    # return render_template('main/index.html', pagination=pagination)


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
            return redirect(url_for('main.add_word', _external=True))
        except IntegrityError:
            db.session.rollback()
            return redirect(url_for('main.add_word', _external=True))
    user_initials = current_user.firstname[0] + current_user.lastname[0]
    return render_template('main/add_word.html', form=form,
                           user_initials=user_initials)


@main.route('/word/<int:word_id>', methods=['GET', 'POST'])
@login_required
def display_word(word_id):
    '''Display a vocabulary word'''

    word = Word.query.get_or_404(word_id)
    return render_template('main/word.html', word=word)


@main.route('/vocabulary')
@login_required
def vocabulary():
    '''Vocabulary route'''

    page = request.args.get('page', 1, type=int)
    words = Word.query.paginate(page=page, per_page=2)
    user_initials = current_user.firstname[0] + current_user.lastname[0]
    return render_template('main/vocabulary.html', words=words,
                           user_initials=user_initials)


@main.app_errorhandler(404)
def page_not_found(error):
    '''404 Page not found'''

    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(error):
    '''500 Internal server error'''

    return render_template('500.html'), 500
