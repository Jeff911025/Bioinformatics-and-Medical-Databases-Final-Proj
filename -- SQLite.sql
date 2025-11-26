-- SQLite
CREATE TABLE IF NOT EXISTS test_table2 (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INTEGER
);

INSERT INTO test_table2 (name, age) VALUES ('Alpha', 25);
INSERT INTO test_table2 (name, age) VALUES ('Beta', 30);


SELECT * FROM Animal WHERE shelter_id = 74;
