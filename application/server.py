from application import app
from flask import render_template, request
from .forms import GenerateForm, Pgmd5Form
import random, string, hashlib

def getChars():
    excludes = app.config['EXCLUDE_CHARS']
    special = list(string.punctuation)
    for x in excludes:
        special.remove(x)
    special = "".join(special)
    return [string.ascii_lowercase,string.ascii_uppercase,string.digits, special]

def passgen(passlength):
    rnd = random.SystemRandom()
    charsets = getChars()
    pwd = []
    while len(pwd) < passlength:
        charset = rnd.choice(charsets)
        pwd.append(rnd.choice(charset))
    return "".join(pwd)

def pgmd5gen(pguser,pgpass):
    return "md5" + hashlib.md5(pgpass.encode('utf-8') + pguser.encode('utf-8')).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    form = GenerateForm()
    if form.validate_on_submit():
        password = passgen(form.passlength.data)
    return render_template('index.html', form=form, password=password)

@app.route('/pgmd5', methods=['GET', 'POST'])
def pgmd5():
    pgmd5 = None
    form = Pgmd5Form()
    if form.validate_on_submit():
        pgmd5 = pgmd5gen(form.pguser.data,form.pgpass.data)
    return render_template('pgmd5.html', form=form, pgmd5=pgmd5)
