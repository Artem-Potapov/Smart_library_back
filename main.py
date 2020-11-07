from flask import Flask
import json
from flask_cors import CORS

file = open('books.json', 'r', encoding='utf-8')
app = Flask(__name__)
CORS(app)
books = json.load(file)


@app.route('/')
def hello_world():
    return json.dumps(books)


@app.route('/authors')
def come():
    return json.dumps([book['author'] for book in books])


app.run()
