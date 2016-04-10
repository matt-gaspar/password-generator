from flask.ext.wtf import Form
from wtforms import DecimalField, SubmitField, StringField
from wtforms.validators import NumberRange

class GenerateForm(Form):
    length = DecimalField('Desired Password Length (minimum 10)',default=15, places=None, validators=[NumberRange(10)])
    submit = SubmitField('Generate')
