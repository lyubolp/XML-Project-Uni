from flask import Flask
from src.xml_document.xml_document import XMLDocument
from src.wiki_api.wiki_api import WikiAPI

app = Flask(__name__)


@app.route('/')
def hello_world():
    get_wiki_content = WikiAPI()
    return get_wiki_content.get_page_header_text_image("Ivan Vazov")


if __name__ == '__main__':
    #app.run()

    #get_wiki_content = WikiAPI()
    #[print(item[1]) for item in get_wiki_content.get_page_text("Ivan Vazov").content]

    parser = XMLDocument()
    parser.open("../alabala.txt")
