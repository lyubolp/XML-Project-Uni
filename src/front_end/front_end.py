from flask import Flask, render_template
from .file_upload_form import FileUploadForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    file_upload_form = FileUploadForm()
    if file_upload_form.validate_on_submit():
        f = file_upload_form.dtd.data
        print(f)
        print(file_upload_form.wiki_article_name)

    print("Error")
    return render_template('index.html', project_name='XML Project', form=file_upload_form)