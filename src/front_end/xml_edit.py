from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class XMLEditForm(FlaskForm):
    download = SubmitField('Сваляне')
