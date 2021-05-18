
DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets 
(
    id SERIAL PRIMARY KEY
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    notes TEXT, 
    available BOOLEAN NOT NULL, DEFAULT TRUE
);

INSERT INTO pets 
    (name, species, photo_url, age, notes, available)
VALUES
    ('Whisky', 'dog','https://unsplash.com/photos/cyimMEASu3A' ,1, 'The one I want', 't'),
    ('Oliver', 'dog','https://images.app.goo.gl/vmNPnuGgFMGcBsj18' 1, 'Deff a must', 't'),
    ('Neko', 'cat','https://unsplash.com/photos/RCfi7vgJjUY' ,1, 'Purrfect', 't'),
    ('Vladimir Purtin', 'cat','https://unsplash.com/photos/75715CVEJhI' ,2, 'Too cute to be true', 't'),
    ('Spiky', 'porcupine','https://unsplash.com/photos/mhlMg2dmn1I' ,3,'Best pal','t');
