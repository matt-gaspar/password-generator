from flask import Flask
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config.Config')
