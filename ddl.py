import sqlite3

# Connectez-vous à la base de données SQLite (ou créez-la si elle n'existe pas)
conn = sqlite3.connect('anime_database.db')

# Créez un objet curseur
cursor = conn.cursor()

# Créez la table 'anime'
cursor.execute('''
CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    title_english TEXT,
    title_japanese TEXT,
    title_synonyms TEXT,
    image_url TEXT,
    type TEXT,
    source TEXT,
    episodes INTEGER,
    status TEXT,
    airing BOOLEAN,
    aired_string TEXT,
    aired TEXT,
    duration TEXT,
    rating TEXT,
    score REAL,
    scored_by INTEGER,
    rank INTEGER,
    popularity INTEGER,
    members INTEGER,
    favorites INTEGER,
    background TEXT,
    premiered TEXT,
    broadcast TEXT,
    related TEXT,
    producer TEXT,
    licensor TEXT,
    studio TEXT,
    genre TEXT,
    opening_theme TEXT,
    ending_theme TEXT
)
''')

# Créez la table 'users'
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    user_id INTEGER,
    user_watching INTEGER,
    user_completed INTEGER,
    user_onhold INTEGER,
    user_dropped INTEGER,
    user_plantowatch INTEGER,
    user_days_spent_watching REAL,
    gender TEXT,
    location TEXT,
    birth_date TEXT,
    access_rank TEXT,
    join_date TEXT,
    last_online TEXT,
    stats_mean_score REAL,
    stats_rewatched INTEGER,
    stats_episodes INTEGER
)
''')

# Créez la table 'ratings'
cursor.execute('''
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    anime_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 10),
    review TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (anime_id) REFERENCES anime(id)
)
''')

# Validez les changements et fermez la connexion
conn.commit()
conn.close()

print("La base de données SQLite avec les tables 'anime', 'users', et 'ratings' a été créée avec succès.")