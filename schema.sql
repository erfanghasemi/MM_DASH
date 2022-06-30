DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,    
    director TEXT NOT NULL,
    rate TEXT NOT NULL,
    movie_description TEXT NOT NULL,
    trailer_url TEXT NOT NULL,
    image_url TEXT NOT NULL
);
