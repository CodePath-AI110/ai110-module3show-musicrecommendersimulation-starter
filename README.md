# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world platforms like Spotify and YouTube predict what you'll love next by blending two approaches: collaborative filtering, which learns from the behavior of millions of similar users (likes, skips, playlists), and content-based filtering, which compares song attributes such as tempo, energy, and mood. My version is purely content-based, since it has no other users' data. It scores each song by how *close* its attributes are to the user's taste profile, rather than rewarding higher or lower values, and then ranks the songs by score to pick the top results. It prioritizes mood first, then genre and energy, with acousticness as a smaller bonus, because mood best captures what a listener wants right now while genre alone is too narrow in a small catalog.

### Features

**`Song`** (loaded from `data/songs.csv`):

- `id`, `title`, `artist`: identifying info, not used in scoring
- `genre`: categorical, matched against the user's favorite genre
- `mood`: categorical, matched against the user's favorite mood
- `energy` (0-1): scored by closeness to the user's target energy
- `acousticness` (0-1): scored against the user's acoustic preference
- `valence`, `tempo_bpm` and `danceability`: stored but not scored in the first version

**`UserProfile`**:

- `favorite_genre`: the genre to match
- `favorite_mood`: the mood to match
- `target_energy` (0-1): the energy level the user wants, so songs are rewarded for being near it
- `likes_acoustic` (bool): whether to favor high or low acousticness

### Algorithm Recipe

**Data flow:**

```
INPUT                    PROCESS (the loop)                      OUTPUT
User Prefs          →    for each song in songs.csv:        →    Ranking
(genre, mood,              score_song(user, song)                sort by score, highest first
 target energy,            → total points + reasons              return the top K
 likes_acoustic)           collect (song, score, reasons)        with an explanation each
```

1. **Input:** a `UserProfile` with a favorite genre, favorite mood, target energy and acoustic preference.
2. **Process:** `load_songs` reads every row of `data/songs.csv`. The loop then judges each song on its own with `score_song`, which returns a total and a list of reasons.
3. **Output:** `recommend_songs` sorts all scored songs from highest to lowest and returns the top K. Each result carries its reasons, so the user can see why it was picked.

**Scoring rule (max 100 points per song):**

| Feature | Rule | Max points |
|---|---|---|
| Mood | Exact match gets full points, otherwise 0 | 35 |
| Genre | Exact match gets full points, otherwise 0 | 25 |
| Energy | `25 × (1 − abs(song.energy − target_energy))` | 25 |
| Acousticness | If `likes_acoustic`: `15 × acousticness`. Otherwise: `15 × (1 − acousticness)` | 15 |

**Why these weights:**

- Mood is worth the most because it matches the listening context. A "chill" listener is happy with lofi, ambient or jazz, but not with a rock song in the wrong mood.
- Genre is worth less because the catalog has 14 genres across 20 songs, so a genre match often points to a single song. At 25 points it still breaks ties between songs that share a mood.
- Energy gives partial credit for closeness instead of all-or-nothing, so near misses on genre or mood can still surface.
- Acousticness is a minor preference that only separates songs that are otherwise close.

### Expected Biases

- **Mood and genre are exact string matches.** A "relaxed" jazz song gets no mood credit for a "chill" user, even though the two moods are close. Great songs with a neighboring mood can be under-ranked.
- **Mood over-prioritization.** Mood plus genre make up 60 points, so a song that matches both can outrank a song that fits the user's energy and acoustic taste perfectly.
- **Genre acts as a filter in a tiny catalog.** With most genres appearing once, users who name a rarer genre (for example, metal or classical) get one strong match and then weak results.
- **Single-value profile.** One favorite genre, one mood and one energy target cannot represent someone with varied taste.
- **Ignored features.** Valence, tempo and danceability are not scored, so two songs with the same score can feel very different.
- **Catalog skew.** Lofi has 3 of the 20 songs and many genres have 1, so some users will always have more good options than others.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
Loading songs from data/songs.csv...
Loaded songs: 20

Recommendations for pop/happy (top 5):

1. Sunrise City by Neon Echo
   Score: 99.20/100
   Reasons: mood match (+35.0); genre match (+25.0); energy similarity (+24.5); acousticness preference (+14.7)

2. Rooftop Lights by Indigo Parade
   Score: 71.75/100
   Reasons: mood match (+35.0); energy similarity (+24.0); acousticness preference (+12.8)

3. Gym Hero by Max Pulse
   Score: 59.50/100
   Reasons: genre match (+25.0); energy similarity (+21.8); acousticness preference (+12.8)

4. Noche de Fuego by Marisol Vega
   Score: 38.80/100
   Reasons: energy similarity (+25.0); acousticness preference (+13.8)

5. Night Drive Loop by Neon Echo
   Score: 38.45/100
   Reasons: energy similarity (+23.8); acousticness preference (+14.7)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


