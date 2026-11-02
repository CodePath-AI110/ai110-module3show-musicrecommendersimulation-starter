"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Taste profile: target values compared against each song's features
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "valence": 0.60,
        "acousticness": 0.20,
    }

    # Contrasting profile, to check the system can tell the two tastes apart
    rock_prefs = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "valence": 0.45,
        "acousticness": 0.10,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(
        f"\nRecommendations for {user_prefs['genre']}/{user_prefs['mood']} "
        f"(top {len(recommendations)}):"
    )
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"\n{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}/100")
        print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
