
from pydantic import BaseModel


# Modèle pour les détails de l'anime
class Anime(BaseModel):
    id: int
    title: str
    title_english: str = None
    title_japanese: str = None
    title_synonyms: str = None
    image_url: str = None
    type: str = None
    source: str = None
    episodes: int = None
    status: str = None
    airing: bool = None
    aired_string: str = None
    aired: str = None
    duration: str = None
    rating: str = None
    score: float = None
    scored_by: int = None
    rank: int = None
    popularity: int = None
    members: int = None
    favorites: int = None
    background: str = None
    premiered: str = None
    broadcast: str = None
    related: str = None
    producer: str = None
    licensor: str = None
    studio: str = None
    genre: str = None
    opening_theme: str = None
    ending_theme: str = None