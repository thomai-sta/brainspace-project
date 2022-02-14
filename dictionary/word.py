from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from dictionary.auth import login_required
from dictionary.db import get_db

bp = Blueprint('word', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        word_name = request.form['word_name']

        if not word_name:
            error = 'Please type in a word'
            flash(error)
        else:
            word_name = str.lower(word_name)

            # Check if word in local DB
            db = get_db()
            word = db.execute(
                'SELECT * FROM word WHERE name = ?', (word_name,)
            ).fetchone()

            if word is None:
                # fetch word from API and automatically save locally
                # @TODO: logged-in user can save manually and have a personilized dictionary, add to "savedby" 
                import requests as req
                url_string = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word_name
                response = req.get(url_string)

                if response.status_code == 200:
                    try:
                        # Save entire json string for later upgrades
                        db.execute(
                            "INSERT INTO word (name, json_string) VALUES (?, ?)",
                            (word_name, response.text),
                        )
                        db.commit()

                        message = "New word. Added to dictionary."
                        flash(message)
                    except db.IntegrityError:
                        error = f"Word already exists."
                        flash(error)
                    return redirect(url_for('word.show', word_name=word_name))
                else:
                    error = "'" + word_name + "' was not found!"
                    flash(error)

            else:
                return redirect(url_for('word.show', word_name=word_name))

    return render_template('word/index.html')


@bp.route('/show/<word_name>', methods=['GET', 'POST'])
def show(word_name):
    db = get_db()
    word = db.execute(
        'SELECT * FROM word WHERE name = ?', (word_name,)
    ).fetchone()
    if word is None:
        error = "Word not in dictionary"
        return redirect(url_for('index'))

    else:
        word_name = word['name']
        json_string = word['json_string']
        import json
        all_data = json.loads(json_string)
        definitions = get_definitions(all_data)

    return render_template('word/show.html', word_name=word_name, definitions=definitions)


@bp.route('/show_all', methods=['GET', 'POST'])
def show_all():
    # more ideas: - select words based on initial letter
    #             - divide dictionary in groups of 10/20 words, so that table doesn't get too long

    db = get_db()
    words = db.execute(
        'SELECT name, json_string FROM word ORDER BY name ASC'
    ).fetchall()

    all_words = {}
    lengths = {}
    for word in words:
        json_string = word['json_string']
        import json
        all_data = json.loads(json_string)
        definitions = get_definitions(all_data)
        lengths[word['name']] = (len(definitions))
        all_words[word['name']] = definitions[0]

    return render_template('word/show_all.html', words=all_words, lengths=lengths)


def get_definitions(data):
    # Get all different definitions
    definitions = []
    for d in data:
        for m in d['meanings']:
            for definition in m['definitions']:
                definitions.append(definition['definition'])

    return definitions
