from os import environ
import requests
from flask import (Blueprint, render_template, redirect,
                   url_for, flash, request, abort)
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func
from application import db
from application.forms import AddEntryForm, UpdateEntryForm, SearchForm
from application.models import Word

main = Blueprint('main', __name__,
                 template_folder='templates',
                 static_folder='static')


@main.route('/')
def index():
    '''Index route'''

    words = Word.query.order_by(func.random()).limit(1)
    return render_template('main/index.html', words=words)


def query_api(word):
    '''Query API for translation'''

    api_key = environ.get('API_KEY')
    url = requests.get(f'{api_key}')
    print(url.status_code)
    return 'Queried API'


@main.route('/translate', methods=['GET', 'POST'])
def translation():
    '''Translate ES => EN or EN => ES'''

    form = SearchForm()
    if form.validate_on_submit():
        if current_user.is_anonymous:
            flash('Please sign in to translate words.', 'warning')
        return redirect(url_for('main.translation'))
    return render_template('main/translation.html', form=form)


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
                        definition4_en=form.definition4_en.data,
                        user_id=current_user.id)
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


@main.route('/word/update/<int:word_id>', methods=['GET', 'POST'])
@login_required
def update_word(word_id):
    '''Update a word'''

    word = Word.query.get_or_404(word_id)
    if word.author != current_user:
        abort(403)
    form = UpdateEntryForm()
    if request.method == 'GET':
        form.word_es.data = word.word_es
        form.sentence1_es.data = word.sentence1_es
        form.sentence1_en.data = word.sentence1_en
        form.sentence2_es.data = word.sentence2_es
        form.sentence2_en.data = word.sentence2_en
        form.sentence3_es.data = word.sentence3_es
        form.sentence3_en.data = word.sentence3_en
        form.definition1_en.data = word.definition1_en
        form.definition2_en.data = word.definition2_en
        form.definition3_en.data = word.definition3_en
        form.definition4_en.data = word.definition4_en
    elif form.validate_on_submit():
        try:
            word.word_es = form.word_es.data
            word.sentence1_es = form.sentence1_es.data
            word.sentence1_en = form.sentence1_en.data
            word.sentence2_es = form.sentence2_es.data
            word.sentence2_en = form.sentence2_en.data
            word.sentence3_es = form.sentence3_es.data
            word.sentence3_en = form.sentence3_en.data
            word.definition1_en = form.definition1_en.data
            word.definition2_en = form.definition2_en.data
            word.definition3_en = form.definition3_en.data
            word.definition4_en = form.definition4_en.data
            db.session.commit()
            db.session.remove()
            flash('Word updated successfully', 'success')
            return redirect(url_for('main.display_word',
                            word_id=word_id, _external=True))
        except IntegrityError:
            db.session.rollback()
            return redirect(url_for('main.update_word', _external=True))
    content = {
            'form': form,
            'word': word
            }
    return render_template('main/update_word.html', **content)


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


@main.route('/mywords')
@login_required
def display_user_words():

    words = Word.query.filter(Word.user_id == current_user.id).all()
    return render_template('main/mywords.html', words=words)


@main.app_errorhandler(404)
def page_not_found(error):
    '''404 Page not found'''

    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(error):
    '''500 Internal server error'''

    return render_template('500.html'), 500
