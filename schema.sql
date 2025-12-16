-- SQLite
CREATE TABLE Animal (
    id  INTEGER PRIMARY KEY,
    sub_id  TEXT,
    kind TEXT,
    variety TEXT,
    sex TEXT,
    bodytype TEXT,
    colour TEXT,
    age INTEGER,
    sterilization TEXT,
    bacterin TEXT,
    foundplace TEXT,
    title TEXT,
    status TEXT,
    opendate TEXT,
    update_at TEXT,
    createtime TEXT,
    album_file TEXT,
    album_update TEXT,
    cDate TEXT,
    adoption_date TEXT,
    shelter_pkid INTEGER REFERENCES Shelter(id),
    adopter_id INTEGER REFERENCES Adopter(id)
);

CREATE TABLE animal_remark (
    id  INTEGER REFERENCES Animal(id),
    remark TEXT
);

CREATE TABLE Shelter (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT
);

CREATE TABLE Adopter (
    id INTEGER PRIMARY KEY,
    phone TEXT,
    name TEXT,
    email TEXT,
    city TEXT, 
    age INTEGER,
    house_type TEXT
);
