# Handoff

## What runs
`.github/workflows/refresh.yml`, daily 11:05 UTC. It reads the first five pages of each listing, merges into the Hugging Face tables by decision page URL, and uploads only if something was added. No LLM.

## What you need
A fork, a Hugging Face dataset to write to (change `REPO` in `src/refresh.py`), and a repo secret `HF_TOKEN` with write access.

## What breaks
- **FLRA changes the page markup.** A page parses to nothing, the run stops, nothing is uploaded, GitHub emails you.
- **More than 50 new decisions in a day** in either listing would push some past page 5. Not plausible for a daily job; rerun the full crawl (`src/crawl.py`, `src/build.py`) to fix it.
- **The FSIP listing's unstable ordering** can hide a decision from a single pass. The full build reads two passes; the daily job doesn't.

## What the data is not
No decision text. Nothing before November 1980 (not on the listing).
