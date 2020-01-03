from flask import Flask, render_template
from .file_upload_form import FileUploadForm
from config import Config
from src.wiki_api.wiki_api import WikiAPI, Content, RequestType
from src.dtd_parser.dtd_parser import DTDParser
from src.xml_generator.xml_generator import XMLGenerator
from src.consts import *


app = Flask(__name__)
app.config.from_object(Config)


def get_content(title: str, request: RequestType) -> Content:
    wiki_getter = WikiAPI()

    if request == RequestType.HEADER_TEXT:
        return wiki_getter.get_page_header_text(title)
    elif request == RequestType.HEADER_IMAGE:
        return wiki_getter.get_page_header_image(title)
    elif request == RequestType.HEADER_TEXT_IMAGE:
        return wiki_getter.get_page_header_text_image(title)
    elif request == RequestType.TEXT:
        return wiki_getter.get_page_text(title)
    elif request == RequestType.IMAGE:
        return wiki_getter.get_page_images(title)
    else:
        raise ValueError("Invalid request type. Valid RequestType is: HEADER_TEXT, HEADER_IMAGE, "
                         "HEADER_TEXT_IMAGE, TEXT or IMAGE")


def __convert_request_literal_to_enum(request_literal: str) -> RequestType:
    if request_literal == HEADER_TEXT_REQUEST_LITERAL:
        return RequestType.HEADER_TEXT
    elif request_literal == HEADER_IMAGE_REQUEST_LITERAL:
        return RequestType.HEADER_IMAGE
    elif request_literal == HEADER_TEXT_IMAGE_REQUEST_LITERAL:
        return RequestType.HEADER_TEXT_IMAGE
    elif request_literal == TEXT_LITERAL:
        return RequestType.TEXT
    elif request_literal == IMAGE_LITERAL:
        return RequestType.IMAGE
    else:
        raise ValueError("Invalid request type. Valid RequestType is: HEADER_TEXT, HEADER_IMAGE, "
                         "HEADER_TEXT_IMAGE, TEXT or IMAGE")


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    file_upload_form = FileUploadForm()
    if file_upload_form.validate_on_submit():
        file_handle = file_upload_form.dtd.data
        dtd_string = file_handle.read()

        request_type = __convert_request_literal_to_enum(file_upload_form.request_type.data)

        parser = DTDParser()
        parser.parse_string(dtd_string.decode('utf-8'))
        xml_generate = XMLGenerator(parser)

        xml_document = xml_generate.generate_xml()
        wiki_content = get_content(file_upload_form.wiki_article_name.data, request_type)

        xml_document.fill_content(wiki_content)

        print(xml_document.to_string())

    return render_template('index.html', project_name='XML Project', form=file_upload_form)