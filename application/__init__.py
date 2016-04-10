from flask import Flask
from flask.ext.bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hxhwodhdo2hdxbq'
app.config['EXCLUDE_CHARS'] = ['$','*']
#app.config['DEFAULT_PWD_LENGTH'] = 15
#app.config['WTF_CSRF_SECRET_KEY'] = 'skdgqheeowi12peu32ywvedi2eugodvc13d'
app.config.from_object(os.environ.get('SETTINGS'))
