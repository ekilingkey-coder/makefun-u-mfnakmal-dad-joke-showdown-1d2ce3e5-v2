# Dad Joke Showdown — entry program

Writes one dad joke to /output/entry.txt, deterministic and offline (Python 3 stdlib only).

- `python3 main.py` writes the entry.
- `python3 main.py --check` reads /output/entry.txt back and reports MATCH or MISMATCH.

The line is `My backpack always has my back.` — see research.md for the candidate pool,
criterion scoring, cold re-score and the adversarial pairwise pass behind the pick.
