"""make.fun Dad Joke Showdown entry (Python 3.13, standard library only).

One original dad joke, at most 200 characters, written to /output/entry.txt.
The grader runs this program with no network, so it only writes the joke.
"""

import os

JOKE = "I asked my smart speaker to tell me a joke. It said, 'I would, but my humor is still buffering.'"

out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
# Deterministic: the same joke is written on every run, twice in grading.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write(JOKE)
