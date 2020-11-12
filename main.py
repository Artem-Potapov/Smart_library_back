from flask import Flask, request
from flask_cors import CORS
import json
books = [{'name': "Детство", 'author': "Л.Н.Толстой",
          'img': 'https://1.bp.blogspot.com/-wWUjjNPVA30/XV7O6j0NwsI/AAAAAAAAAIk/a9zxrJFhPbAvhoReUPvrylLhXpoEAbAjACLcBGAs/s1600/3eb7fe8839702db7e1dd1133a873e8cb.jpg',
          'rate': 4.5,
          'download': 'https://cdn.discordapp.com/attachments/767038798034501653/770925030728663040/5f6c97a57cfe29c7.txt'},
         {'name': "Черная курица", 'author': "Антоний Погорельский",
          'img': 'https://7960777a-2fd1-4b07-8bbb-896e98c4659c.selcdn.net/upload/prod_add4/961/product-360961-1.jpg',
          'rate': 4,
          'download': 'https://cdn.discordapp.com/attachments/767038798034501653/770924792399921193/d98b76878eb69dd7.txt'},
         {'name': "В дурном обществе", 'author': "Владимир Короленко",
          'img': 'https://kapital-knigi.ru/assets/images/products/11893/9785222321089.jpg', 'rate': 5,
          'download': 'https://cdn.discordapp.com/attachments/767038798034501653/770924061701701652/698f1a897b34ef5b.txt'}]

print(list(filter(lambda book: book['author'] == 'Л.Н.Толстой', books)))


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'hello from backend'


@app.route('/authors')
def authors():
    return json.dumps([book['author'] for book in books])


@app.route('/test')
def test():
    return request.args.get('author', 'empty')


app.run()
