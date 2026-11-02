import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into dictionaries with numeric features."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    numeric_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and explain each contribution."""
    score = 0.0
    reasons = []

    if song["mood"] == user_prefs["mood"]:
        score += 35
        reasons.append("mood match (+35.0)")

    if song["genre"] == user_prefs["genre"]:
        score += 25
        reasons.append("genre match (+25.0)")

    energy_score = 25 * (1 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.1f})")

    if "likes_acoustic" in user_prefs:
        acoustic_score = (
            15 * song["acousticness"]
            if user_prefs["likes_acoustic"]
            else 15 * (1 - song["acousticness"])
        )
    else:
        acoustic_score = 15 * (
            1 - abs(song["acousticness"] - user_prefs["acousticness"])
        )
    score += acoustic_score
    reasons.append(f"acousticness preference (+{acoustic_score:.1f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top recommendations with explanations."""
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    scored_songs.sort(key=lambda result: (-result[1], result[0]["id"]))
    return scored_songs[:k]
