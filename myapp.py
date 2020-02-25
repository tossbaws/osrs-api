import flask
from flask_cors import CORS
import requests
import json

app = flask.Flask(__name__)
CORS(app)


# Run this using $ gunicorn -w 2 myapp:app
@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')


@app.route('/<letter>/<pgno>', methods=['GET', 'POST'])
def get_pages(letter, pgno):
    url = 'http://services.runescape.com/m=itemdb_oldschool'
    cata = '/api/catalogue/items.json?category=1&alpha='
    response = requests.get(url + cata + letter + '&page=' + pgno)

    print(json.dumps(response.json()))

    # return revised.json()
    return response.json()


@app.route('/<id>', methods=['GET', 'POST'])
def get_item(id):
    url = 'http://services.runescape.com/m=itemdb_oldschool'
    suff = '/api/catalogue/detail.json?item='

    response = requests.get(url + suff + id)

    return response.json()


if __name__ == '__main__':
    app.run()
