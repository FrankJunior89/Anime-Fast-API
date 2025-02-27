from fastapi import FastAPI, HTTPException,APIRouter
import sqlite3
from pydantic import BaseModel
from user import User

router = APIRouter()

@router.post("/users/")
def create_user(user: User):
    conn = sqlite3.connect('anime_database.db')
    cursor = conn.cursor()
    try:
        # Vérifier si l'utilisateur existe déjà
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user.user_id,))
        existing_user = cursor.fetchone()
        if existing_user:
            raise HTTPException(status_code=400, detail="User ID already registered")

        # Insérer le nouvel utilisateur
        cursor.execute('''
            INSERT INTO users (
                username, user_id, user_watching, user_completed, user_onhold, user_dropped, user_plantowatch,
                user_days_spent_watching, gender, location, birth_date, access_rank, join_date, last_online,
                stats_mean_score, stats_rewatched, stats_episodes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user.username, user.user_id, user.user_watching, user.user_completed, user.user_onhold, user.user_dropped,
            user.user_plantowatch, user.user_days_spent_watching, user.gender, user.location, user.birth_date,
            user.access_rank, user.join_date, user.last_online, user.stats_mean_score, user.stats_rewatched,
            user.stats_episodes
        ))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating user: {e}")
    finally:
        conn.close()
    return {"message": "User created successfully"}

# Route pour obtenir les détails d'un utilisateur par ID
@router.get("/user/{user_id}", response_model=User)
async def get_user(user_id: int):
    conn = sqlite3.connect('anime_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        user = User(
            id=row[0],
            username=row[1],
            user_id=row[2],
            user_watching=row[3],
            user_completed=row[4],
            user_onhold=row[5],
            user_dropped=row[6],
            user_plantowatch=row[7],
            user_days_spent_watching=row[8],
            gender=row[9],
            location=row[10],
            birth_date=row[11],
            access_rank=row[12],
            join_date=row[13],
            last_online=row[14],
            stats_mean_score=row[15],
            stats_rewatched=row[16],
            stats_episodes=row[17]
        )
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
    

@router.get("/get_recommendations/")
async def plan_to_watch(user_id: int):
    pass