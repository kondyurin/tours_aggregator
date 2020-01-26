from flask import Flask, render_template
from flask import request

from data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', subtitle=subtitle, description=description, tours=tours)

@app.route('/tour/<int:id>/')
def tour(id):
    return render_template('tour.html', id=id, tours=tours, departures=departures)

@app.route('/direction/<country>/')
def direction(country):
    country_tours = [values for values in tours.values() if values['departure'] == country]
    country_tours_price = [values['price'] for values in tours.values() if values['departure'] == country]
    country_tours_nights = [values['nights'] for values in tours.values() if values['departure'] == country]

    return render_template('direction.html', country=country, tours=tours, departures=departures, country_tours=country_tours, country_tours_price=country_tours_price, country_tours_nights=country_tours_nights)

# @app.route('/book/<author>/<title>')
# def book(author, title):
#     return "Здесь будет страница книги " + title + " автора " + author

# @app.route('/search/')
# def search():
#     return "Выполняем поиск по строке " + request.values.get("s")

@app.errorhandler(404)
def not_found(e):
    return "404 Not Found"

@app.errorhandler(500)
def server_error(e):
    return "500 Internal Server Error"
    
app.run('0.0.0.0', 8000, debug=True)