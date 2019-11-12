from flask import Flask
from src.XMLDocument import XMLDocument

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    #app.run()
    print("Hello world!")

    obj = XMLDocument()

    obj.open("sample.xml")
    #obj.add_element("items", "item2", "item3abc", {"name": "item3"})
    obj.save()
