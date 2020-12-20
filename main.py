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
    if filters.get('genre'):
        _books = list(filter(lambda book: book.get('genre') == filters.get('genre'), _books))
    return json.dumps(_books)


@app.route('/authors')
def come():
    authors = set()
    for book in books:
        authors.add(book['author'])
    return json.dumps(list(authors))


@app.route('/genres')
def give_genre():
    genre = set()
    for book in books:
        genre.add(book['genre'])
    return json.dumps(list(genre))


@app.route('/ages')
def give_ages():
    ages = set()
    for book in books:
        ages.add(book['age'])
    return json.dumps(list(ages))


@app.route('/rates_from5')
def give_rate_from5():
    ageper5 = set()
    for book in books:
        ageper5.add(book['rate_f5'])
    return json.dumps(list(ageper5))


app.run()
