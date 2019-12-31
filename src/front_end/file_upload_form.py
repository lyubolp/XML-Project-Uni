from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired


class FileUploadForm(FlaskForm):
    dtd = FileField(validators=[FileRequired()])
    wiki_article_name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Генериране')
