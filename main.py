from flask import Flask
import json
from flask_cors import CORS
from flask import request

file = open('books.json', 'r', encoding='utf-8')
app = Flask(__name__)
CORS(app)
books = json.load(file)


@app.route('/books')
def give_books():
    filters = json.loads(request.args.get('filters', '{}'))
    _books = []

    for book in books:
        if not filters.get('author') or book.get('author') == filters.get('author'):
            _books.append(book)

    return json.dumps(_books)


@app.route('/authors')
def come():
    return json.dumps([book['author'] for book in books])


@app.route('/test')
def test():
    return request.args.get('data', 'ke5k')


app.run()
