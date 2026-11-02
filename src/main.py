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

    # Original taste profiles, plus an additional profile for comparison.
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "valence": 0.60,
        "acousticness": 0.20,
    }
    rock_prefs = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "valence": 0.45,
        "acousticness": 0.10,
    }
    lofi_prefs = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "acousticness": 0.80,
    }
    profiles = {
        "High-Energy Pop": user_prefs,
        "Deep Intense Rock": rock_prefs,
        "Chill Lofi": lofi_prefs,
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{profile_name} ({user_prefs['genre']}/{user_prefs['mood']})")
        print(f"Top {len(recommendations)} recommendations:")
        for index, (song, score, explanation) in enumerate(
            recommendations, start=1
        ):
            print(f"{index}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}/100")
            print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
