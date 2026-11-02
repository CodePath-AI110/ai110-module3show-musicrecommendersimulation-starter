# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Goal / Task

VibeMatch suggests songs a listener might like. It does not predict a rating. It picks the top 5 songs from a small catalog. It does this by matching a listener's taste profile to each song. The profile has a favorite genre, a favorite mood, a target energy, and an acoustic preference.

---

## 3. Data Used

- The catalog has 20 songs in `data/songs.csv`.
- Each song has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.
- There are 17 genres. Lofi has 3 songs and pop has 2. Every other genre has only 1.
- There are 16 moods. Chill has 3 songs. Happy and intense have 2 each. The rest have 1.
- I did not add or remove songs from the starter data.
- The data is tiny and made up. It has no lyrics, language, or release year. It also has no listening history from real people.

---

## 4. Algorithm Summary

VibeMatch gives each song a score out of 100. Then it sorts the songs from best to worst.

- **Mood match:** up to 35 points. The song's mood must match exactly.
- **Genre match:** up to 25 points. The song's genre must match exactly.
- **Energy:** up to 25 points. The closer the song is to the target energy, the more points it gets.
- **Acousticness:** up to 15 points. Songs that fit the acoustic preference get more points.

Mood and genre count the most. An exact match is a strong sign of what the listener wants. Energy gives partial credit, so close songs still score well. Each result also lists the points it earned, so you can see why it was picked.

Valence, tempo, and danceability are in the data. The score does not use them.

---

## 5. Observed Behavior / Biases

- Exact mood and genre matches beat songs that are closer in energy or acousticness. A song with the wrong label can lose even if it sounds right.
- This can make a filter bubble. Listeners keep getting the same few moods and genres. They do not find related music.
- The catalog is small and uneven. Lofi fans have 3 strong choices. Fans of a genre with only 1 song run out of good matches fast.
- Gym Hero showed up for both the pop and rock profiles. It is pop, but it has an intense mood and high energy. That was enough to rank it high for rock.
- Related labels get no credit. "Chill" and "relaxed" count as totally different moods.

---

## 6. Evaluation Process

I tested three profiles:

- **High-Energy Pop:** pop, happy, energy 0.80, less acoustic.
- **Deep Intense Rock:** rock, intense, energy 0.92, very low acousticness.
- **Chill Lofi:** lofi, chill, energy 0.40, more acoustic.

For each profile, I checked if the top songs matched the mood, genre, energy, and acoustic preference. The results mostly made sense.

I also compared the profiles with each other:

- **Pop vs. Rock:** Sunrise City won for pop. It matches pop and happy. Storm Runner won for rock. It matches rock and intense. Gym Hero was in both lists.
- **Pop vs. Lofi:** The list changed from upbeat songs like Sunrise City and Rooftop Lights to quiet songs like Midnight Coding and Library Rain.
- **Rock vs. Lofi:** Rock favored loud songs like Storm Runner. Lofi favored calm songs like Midnight Coding and Spacewalk Thoughts. This is what I expected, since the two profiles want opposite things.

The only surprise was Gym Hero.

---

## 7. Intended Use and Non-Intended Use

**Intended use**

- Classroom learning about how recommenders work.
- Trying out simple scoring rules and seeing how they change results.
- Showing clear reasons for each recommendation.

**Not intended for**

- A real music app with real users. The catalog is far too small.
- Deciding what artists get heard or paid.
- Judging a person's taste. It only sees four preferences.
- Listeners whose taste mixes many genres or moods.

---

## 8. Ideas for Improvement

1. **Give partial credit for related labels.** For example, "chill" and "relaxed" should score close to each other. The same goes for "pop" and "indie pop".
2. **Use more features.** Valence, tempo, and danceability are already in the data. Adding them would catch songs that sound right but have a different label.
3. **Mix up the top results.** Add a rule so the top 5 are not all from one genre or mood. This would help break the filter bubble. A bigger catalog would help too.

---

## 9. Personal Reflection

**Biggest learning moment.** My biggest lesson was that the weights are the design. I gave mood 35 points and genre 25. After that, nearly every result followed from those two numbers. A song with the right label beat a song that sounded closer. I only saw this when I ran three very different profiles and compared the lists.

**How AI helped, and when I double-checked it.** AI helped me move fast. It helped me set up the scoring, the command-line output, and the model card. But I could not trust it blindly. I checked the numbers against `data/songs.csv`. For example, I counted the genres and moods myself. I also checked that the card matched the code. The profiles set a valence value, but the score never uses it. A tool can write something that sounds right and is slightly wrong. Reading the output was my job.

**What surprised me.** A few simple rules felt like real recommendations. Sunrise City came first for pop. Midnight Coding came first for lofi. It felt like the system "got" the vibe. Then Gym Hero showed up for both pop and rock. That broke the illusion. The system was only adding points. It did not understand music.

**What I would try next.**

- Give partial credit for related moods and genres.
- Use valence, tempo, and danceability in the score.
- Add a rule to mix up the top 5.
- Grow the catalog, so more genres have more than one song.
