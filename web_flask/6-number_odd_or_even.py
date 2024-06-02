#!/usr/bin/pyhton3
"""
Starts flask app
"""

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def index():
    """ PAGE INDEX - HELLO HBNB """
    return 'HELLO HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ PAGE HBNB - HBNB """
    return 'HBHB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ Displays C + <text> -> (format _ to "space") """
    return 'C' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """ Displays Pyhton + <text> -> (format _ to "space" = DEFAULT : is cool) """
    return 'Pyhton' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """ Display n : number ; only if n is an integer"""
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """  Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        ev = 'even'
    else:
        ev = 'odd'
    return render_template('6-number_odd_or_even.html',
                            n=n,
                            ev=ev)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
                                                                                                                    