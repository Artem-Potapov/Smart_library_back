from flask import Flask
import json
from flask_cors import CORS
from flask import request
from urllib.parse import unquote
import os

file = open('boos.json', 'r', encoding='utf-8')
app = Flask(__name__)
CORS(app)


@app.route('/upload')
def load():
    books = request.args.get("books", '[]')
    book_file = open("boos.json", "w+")
    book_file.write(books)
    return ''

@app.route('/books')
def give_books():
    books = json.load(file)
    filters = json.loads(request.args.get('filters', '{}'))
    _books = books

    if filters.get('author'):
        _books = list(filter(lambda book: book.get('author') == filters.get('author'), _books))
    if filters.get('genre'):
        _books = list(filter(lambda book: book.get('genre') == filters.get('genre'), _books))
    if filters.get('rating'):
        _books = list(filter(lambda book: book.get('rate') >= int(filters.get('rating')), _books))
    return json.dumps(_books)


@app.route('/authors')
def come():
    books = json.load(file)
    authors = set()
    for book in books:
        authors.add(book['author'])
    return json.dumps(list(authors))


@app.route('/genres')
def give_genre():
    books = json.load(file)
    genre = set()
    for book in books:
        genre.add(book['genre'])
    return json.dumps(list(genre))


@app.route('/ages')
def give_ages():
    books = json.load(file)
    ages = set()
    for book in books:
        ages.add(book['age'])
    return json.dumps(list(ages))


@app.route('/favbooks')
def give_favbooks():
    books = json.load(file)
    print(unquote(request.args.get('testresult')))
    filters = json.loads(unquote(request.args.get('testresult')))

    _books = books
    if filters.get('authors') and filters.get('authors')[0] != 'all':
        _books = list(filter(lambda book: book.get('author') in filters.get('authors'), _books))
    if filters.get('genres') and filters.get('genres')[0] != 'all':
        _books = list(filter(lambda book: book.get('genre') in filters.get('genres'), _books))
    if filters.get('age'):
        _books = list(filter(lambda book: int(book.get('age')[0:-1]) <= filters.get('age'), _books))

    return json.dumps(_books)


app.run()