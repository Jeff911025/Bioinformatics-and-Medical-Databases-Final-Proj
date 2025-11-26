CREATE TABLE IF NOT EXISTS Animal (
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
    remark TEXT,
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

CREATE TABLE IF NOT EXISTS Shelter (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    email TEXT
);
CREATE TABLE IF NOT EXISTS Adopter (
    adopter_phone TEXT PRIMARY KEY,
    name TEXT,
    email TEXT
);  

SELECT * FROM Animal;
