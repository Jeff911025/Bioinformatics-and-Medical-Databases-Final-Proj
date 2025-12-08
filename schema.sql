-- SQLite
CREATE TABLE Animal (
    id  INTEGER PRIMARY KEY,
    sub_id  TEXT,
    place TEXT,
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
    caption TEXT,
    opendate TEXT,
    closeddate TEXT,
    update_at TEXT,
    createtime TEXT,
    album_file TEXT,
    album_update TEXT,
    cDate TEXT,
    adoption_date TEXT,
    shelter_pkid INTEGER REFERENCES Shelter(id),
    adopter_phone TEXT REFERENCES Adopter(adopter_phone)
);

CREATE TABLE animal_remark (
    id  INTEGER REFERENCES Animal(id),
    remark TEXT
);

CREATE TABLE Shelter (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    email TEXT
);

CREATE TABLE Adopter (
    adopter_phone TEXT PRIMARY KEY,
    name TEXT,
    email TEXT
);
