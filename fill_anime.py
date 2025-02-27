import sqlite3
import csv

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect('anime_database.db')
cursor = conn.cursor()

# Fonction pour insérer des lignes à partir d'un fichier CSV dans la table anime
def insert_anime_from_csv(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cursor.execute('''
                    INSERT INTO anime (
                        title, title_english, title_japanese, title_synonyms, image_url, type, source, episodes, status,
                        airing, aired_string, aired, duration, rating, score, scored_by, rank, popularity, members,
                        favorites, background, premiered, broadcast, related, producer, licensor, studio, genre,
                        opening_theme, ending_theme
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['title'], row['title_english'], row['title_japanese'], row['title_synonyms'], row['image_url'],
                    row['type'], row['source'], int(row['episodes']), row['status'], bool(row['airing']),
                    row['aired_string'], row['aired'], row['duration'], row['rating'], float(row['score']),
                    int(float(row['scored_by'])), int(float(row['rank'])), int(float(row['popularity'])), int(float(row['members'])),
                    int(float(row['favorites'])), row['background'], row['premiered'], row['broadcast'], row['related'],
                    row['producer'], row['licensor'], row['studio'], row['genre'], row['opening_theme'],
                    row['ending_theme']
                ))
            except Exception as e:
                print(f"Error inserting row: {row}")
                print(f"Exception: {e}")

# Exemple d'utilisation
csv_file_path = 'animes.csv'  # Remplacez par le chemin vers votre fichier CSV
insert_anime_from_csv(csv_file_path)

# Validez les changements et fermez la connexion
conn.commit()
conn.close()

print("Les lignes du fichier CSV ont été insérées avec succès dans la table 'anime'.")