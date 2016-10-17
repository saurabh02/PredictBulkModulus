from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class MaterialForm(Form):
    formula = StringField('formula', validators=[DataRequired()])
    # Add additional fields here
