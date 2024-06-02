#!/usr/bin/python3
"""
Starts flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ PAGE INDEX - HELLO HBNB """
    return 'HELLO HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ PAGE HBNB - HBNB """
    return 'HBHB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
