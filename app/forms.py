from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired


class MaterialForm(Form):
    formula = StringField('formula', validators=[DataRequired()])
    # Add additional fields here
