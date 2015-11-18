DROP TABLE IF EXISTS entries;
CREATE TABLE entries (
  id    INTEGER PRIMARY KEY autoincrement,
  title TEXT NOT NULL,
  text  TEXT NOT NULL
);