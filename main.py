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
    _books = books

    if filters.get('author'):
        _books = list(filter(lambda book: book.get('author') == filters.get('author'), _books))

    return json.dumps(_books)


@app.route('/authors')
def come():
    authors = set()
    for book in books:
        authors.add(book['author'])
    return json.dumps(list(authors))


@app.route('/test')
def test():
    return request.args.get('data', 'ke5k')


app.run()
