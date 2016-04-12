from flask.ext.wtf import Form
from wtforms import DecimalField
from wtforms.validators import NumberRange, Required

class GenerateForm(Form):
    passlength = DecimalField('Desired Password Length (10 - 30)', default=15, places=None, validators=[NumberRange(10,30), Required()])
