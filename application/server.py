from application import app
from flask import render_template
from .forms import GenerateForm, Pgmd5Form
import random, string, hashlib


def getCharSets(alphanumeric):
    excludes = list(app.config['EXCLUDE_CHARS'])
    # Removes characters that we don't want to be used in a password
    # Returns character sets as strings, special characters manipulated as above
    # if they are to be included (alphanumeric = false)
    if alphanumeric:
        return [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    special = [x for x in list(string.punctuation) if x not in excludes]
    special = "".join(special)
    return [string.ascii_lowercase, string.ascii_uppercase, string.digits, special]


def passgen(passlength, alphanumeric):
    rnd = random.SystemRandom()
    charsets = getCharSets(alphanumeric)
    pwd = []
    while len(pwd) < passlength:
        # Select a character set to use
        charset = rnd.choice(charsets)
        # and a character from the selected set
        pwd.append(rnd.choice(charset))
    return "".join(pwd)


def pgmd5gen(pguser, pgpass):
    # Postgresql uses md5 hash of the concatentation of the user password and user name
    return "md5" + hashlib.md5(pgpass.encode('utf-8') + pguser.encode('utf-8')).hexdigest()


@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    form = GenerateForm()
    if form.validate_on_submit():
        password = passgen(form.passlength.data, form.alphanumeric_selector.data)
    return render_template('index.html', form=form, password=password)


@app.route('/pgmd5', methods=['GET', 'POST'])
def pgmd5():
    pgmd5 = None
    form = Pgmd5Form()
    if form.validate_on_submit():
        pgmd5 = pgmd5gen(form.pguser.data, form.pgpass.data)
    return render_template('pgmd5.html', form=form, pgmd5=pgmd5)
