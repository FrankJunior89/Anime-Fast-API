from fastapi import FastAPI, HTTPException,APIRouter
import sqlite3
from pydantic import BaseModel
from anime import Anime

router = APIRouter()

# Route pour obtenir les détails d'un anime par ID
@router.get("/anime/{anime_id}", response_model=Anime)
async def get_anime(anime_id: int):
    conn = sqlite3.connect('anime_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM anime WHERE id=?", (anime_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        anime = Anime(
            id=row[0],
            title=row[1],
            title_english=row[2],
            title_japanese=row[3],
            title_synonyms=row[4],
            image_url=row[5],
            type=row[6],
            source=row[7],
            episodes=row[8],
            status=row[9],
            airing=bool(row[10]),
            aired_string=row[11],
            aired=row[12],
            duration=row[13],
            rating=row[14],
            score=row[15],
            scored_by=row[16],
            rank=row[17],
            popularity=row[18],
            members=row[19],
            favorites=row[20],
            background=row[21],
            premiered=row[22],
            broadcast=row[23],
            related=row[24],
            producer=row[25],
            licensor=row[26],
            studio=row[27],
            genre=row[28],
            opening_theme=row[29],
            ending_theme=row[30]
        )
        return anime
    else:
        raise HTTPException(status_code=404, detail="Anime not found")
    

# Route pour ajouter une évaluation
@router.post("/rate_anime/")
async def rate_anime(user_id: int, anime_id: int, rating: int, review: str = None):
    conn = sqlite3.connect('anime_database.db')
    cursor = conn.cursor()
    try:
        # Vérifier si l'évaluation existe déjà
        cursor.execute('''
            SELECT * FROM ratings WHERE user_id = ? AND anime_id = ?
        ''', (user_id, anime_id))
        existing_rating = cursor.fetchone()

        if existing_rating:
            # Mettre à jour l'évaluation existante
            cursor.execute('''
                UPDATE ratings
                SET rating = ?, review = ?
                WHERE user_id = ? AND anime_id = ?
            ''', (rating, review, user_id, anime_id))
            message = "Rating updated successfully"
        else:
            # Insérer une nouvelle évaluation
            cursor.execute('''
                INSERT INTO ratings (user_id, anime_id, rating, review)
                VALUES (?, ?, ?, ?)
            ''', (user_id, anime_id, rating, review))
            message = "Rating added successfully"

        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error inserting/updating rating: {e}")
    finally:
        conn.close()
    return {"message": message}

@router.post("/plan_to_watch/")
async def plan_to_watch(user_id: int, anime_id: int):
    conn = sqlite3.connect('anime_database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE users
            SET user_plantowatch = user_plantowatch + 1
            WHERE user_id = ?
        ''', (user_id,))
        conn.commit()
        print(f"{user_id} plans to watch {anime_id}")
    except Exception as e:
        print(f"Error updating user_plantowatch for user_id: {user_id}")
        print(f"Exception: {e}")
    conn.commit()
    conn.close()

@router.post("/complete_anime/")
async def complete_anime(user_id: int, anime_id: int):
    pass

@router.post("/drop_anime/")
async def drop_anime(user_id: int, anime_id: int):
    pass

@router.get("/predict_rating/")
async def predict_rating(anime_id: int):
    pass
