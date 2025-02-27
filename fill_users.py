import sqlite3
import csv

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect('anime_database.db')
cursor = conn.cursor()

# Fonction pour insérer des lignes à partir d'un fichier CSV dans la table users
def insert_users_from_csv(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cursor.execute('''
                    INSERT INTO users (
                        username, user_id, user_watching, user_completed, user_onhold, user_dropped, user_plantowatch,
                        user_days_spent_watching, gender, location, birth_date, access_rank, join_date, last_online,
                        stats_mean_score, stats_rewatched, stats_episodes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['username'], int(row['user_id']), int(row['user_watching']), int(row['user_completed']),
                    int(row['user_onhold']), int(row['user_dropped']), int(row['user_plantowatch']),
                    float(row['user_days_spent_watching']), row['gender'], row['location'], row['birth_date'],
                    row['access_rank'], row['join_date'], row['last_online'], float(row['stats_mean_score']),
                    int(row['stats_rewatched']), int(row['stats_episodes'])
                ))
            except Exception as e:
                print(f"Error inserting row: {row}")
                print(f"Exception: {e}")

# Exemple d'utilisation
csv_file_path = 'users.csv'  # Remplacez par le chemin vers votre fichier CSV
insert_users_from_csv(csv_file_path)

# Validez les changements et fermez la connexion
conn.commit()
conn.close()

print("Les lignes du fichier CSV ont été insérées avec succès dans la table 'users'.")