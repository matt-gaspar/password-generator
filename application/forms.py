from flask.ext.wtf import Form
from wtforms import DecimalField, StringField
from wtforms.validators import NumberRange, Required

class GenerateForm(Form):
    passlength = DecimalField('Desired Password Length (10 - 30)', default=15, places=None, validators=[NumberRange(10,30), Required()])

class Pgmd5Form(Form):
    pguser = StringField('Postgres User Name')
    pgpass = StringField('Postgres Password')
