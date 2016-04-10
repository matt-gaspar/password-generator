from flask.ext.wtf import Form
from wtforms import DecimalField, SubmitField, StringField

class GenerateForm(Form):
    length = DecimalField('Password Length (default=15)')
    submit = SubmitField('Generate')
    
