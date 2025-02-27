import sqlite3

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect('anime_database.db')
cursor = conn.cursor()

# Fonction pour tester l'importation des données dans la table anime
def test_import():
    try:
        cursor.execute("SELECT COUNT(*) FROM anime")
        count = cursor.fetchone()[0]
        print(f"Nombre de lignes dans la table anime: {count}")

        # Récupérer et afficher quelques lignes pour vérifier l'importation
        cursor.execute("SELECT * FROM anime LIMIT 1")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.OperationalError as e:
        print(f"Erreur: {e}")

# Exécuter le test
test_import()

# Fermer la connexion
conn.close()