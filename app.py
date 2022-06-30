from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_movie(movie_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM movies WHERE id = ?',
                        (movie_id,)).fetchone()
    conn.close()
    return post

@app.route('/', methods=['GET'])
def return_all_movies():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return render_template('homepage.html', movies=movies)

@app.route('/movies/<movie_id>', methods=['GET'])
def return_specific_movies(movie_id):
    movie = get_movie(movie_id)
    return render_template('movie.html', movie=movie)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8000)