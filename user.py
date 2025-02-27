from pydantic import BaseModel

# Modèle pour les détails de l'utilisateur
class User(BaseModel):
    id: int
    username: str
    user_id: int
    user_watching: int
    user_completed: int
    user_onhold: int
    user_dropped: int
    user_plantowatch: int
    user_days_spent_watching: float
    gender: str = None
    location: str = None
    birth_date: str = None
    access_rank: str = None
    join_date: str = None
    last_online: str = None
    stats_mean_score: float = None
    stats_rewatched: int = None
    stats_episodes: int = None