from application import app
from flask import render_template, request
from .forms import GenerateForm
import random, string

def getChars():
    excludes = app.config['EXCLUDE_CHARS']
    letters = string.ascii_letters
    digits = string.digits
    special = list(string.punctuation)
    for x in excludes:
        special.remove(x)
    special = "".join(special)
    return [letters, digits, special]


def passgen(length=15):
    rnd = random.SystemRandom()
    charsets = getChars()
    pwd = []
    while len(pwd) < length:
        charset = rnd.choice(charsets)
        pwd.append(rnd.choice(charset))
    return "".join(pwd)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    form = GenerateForm()
    if form.validate_on_submit():
        password = passgen(form.length.data)
        form.length.data = ''
    return render_template('index.html', form=form, password=password)
