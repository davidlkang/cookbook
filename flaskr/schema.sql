CREATE TABLE recipes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  recipe TEXT
);

CREATE TABLE units (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE ingredients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  unit_id INTEGER NOT NULL,
  FOREIGN KEY (unit_id) REFERENCES units (id)
);

CREATE TABLE recipes__ingredients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_id INTEGER NOT NULL,
  ingredient_id INTEGER NOT NULL,
  amount INTEGER,
  FOREIGN KEY (recipe_id) REFERENCES recipes (id),
  FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
);
