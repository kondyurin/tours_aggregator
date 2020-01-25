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

@app.route('/direction/')
def direction():
    return render_template('direction.html')

@app.route('/videos/<id>')
def videos_item(id):
    return "Здесь будет видео" + id

@app.route('/book/<author>/<title>')
def book(author, title):
    return "Здесь будет страница книги " + title + " автора " + author

@app.route('/search/')
def search():
    return "Выполняем поиск по строке " + request.values.get("s")

@app.errorhandler(404)
def not_found(e):
    return "404 Not Found"

@app.errorhandler(500)
def server_error(e):
    return "500 Internal Server Error"
    
app.run('0.0.0.0', 8000, debug=True)