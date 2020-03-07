from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ParametersForm(FlaskForm):
    param = StringField('Parameter_name', [DataRequired()])
    submit = SubmitField('Submit')

class ProceedForm(FlaskForm):
    submit = SubmitField('Go')
