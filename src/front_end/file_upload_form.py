from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired
from src.consts import *


class FileUploadForm(FlaskForm):
    dtd = FileField(validators=[FileRequired()])
    wiki_article_name = StringField('Name', validators=[DataRequired()])
    request_type = RadioField('Изберете каква информация да се вземе',
                              choices=[(HEADER_TEXT_REQUEST_LITERAL, 'Взима заглавията на секциите и текста'),
                                       (HEADER_IMAGE_REQUEST_LITERAL, 'Взема заглавията на секциите и изображенията'),
                                       (HEADER_TEXT_IMAGE_REQUEST_LITERAL, 'Взема заглавията на секциите, '
                                                                         'текста и изображенията'),
                                       (TEXT_LITERAL, 'Взема само текста'),
                                       (IMAGE_LITERAL, 'Взема само изображенията')],
                              default=1)
    submit = SubmitField('Генериране')
