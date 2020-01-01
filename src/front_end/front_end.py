from flask import Flask, render_template
from .file_upload_form import FileUploadForm
from config import Config
from src.wiki_api.wiki_api import WikiAPI, Content

app = Flask(__name__)
app.config.from_object(Config)


def get_content(title: str) -> Content:
    wiki_getter = WikiAPI()
    return wiki_getter.get_page_header_text(title)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    file_upload_form = FileUploadForm()
    if file_upload_form.validate_on_submit():
        file_handle = file_upload_form.dtd.data
        print(file_handle.read())
        wiki_content = get_content(file_upload_form.wiki_article_name.data)

    return render_template('index.html', project_name='XML Project', form=file_upload_form)