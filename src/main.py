from flask import Flask
from src.XMLDocument import XMLDocument
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    #app.run()

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": "Ferrari",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    html_data = DATA["parse"]["text"]["*"]

    parser = XMLDocument()

    #parser.open("sample.xml")
    parser.open_from_string("<html>" + html_data + "</html>")

    content = parser.get_elements("p")

    for el in content:
        striped_text = [text.strip() for text in list(el.itertext())]
        formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                         and item != '\n' and item != '']

    result: str = ""
    for el in formated_text:
        result = result + " " + el

    print(result)
