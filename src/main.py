from flask import Flask
from src.XMLDocument import XMLDocument

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    #app.run()

    obj = XMLDocument()

    obj.open("sample.xml")
    print(obj.get_elements("item")[1].attrib)
    obj.save()
