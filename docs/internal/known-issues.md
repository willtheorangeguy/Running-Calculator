# Known Issues — Running-Calculator

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.

**3 open:** 2 medium, 1 low.

## 1. A total time of zero divides by zero and exits with a traceback

**Severity:** Medium
**Where:** `main.py` -> `main`, `metersps = distance / time`

**What:** `time = (hours * 3600) + (mins * 60) + secs`, then `metersps = distance / time` with no check that `time` is non-zero. Entering `0` for hours, minutes, and seconds raises `ZeroDivisionError: float division by zero` and the program exits with a traceback. Verified by running it. The `try/except ValueError` around the four inputs catches non-numeric entry but not this.

**Why it matters:** The prompts actively invite the input that causes it: two of them read 'if < 1, enter 0'. Someone trying the program out, or checking what it does with a trivial case, will enter zeros and get a Python traceback rather than a message -- and because the crash exits rather than re-prompting, the whole session is lost including any earlier runs they had done in the loop. Every other bad input in this program is handled politely, which makes the one that is not more surprising.

**Suggested fix:** Guard before dividing: if `time <= 0`, print a sentence and re-prompt through the existing `time_run` loop, which is already there for the `ValueError` path. Negative values deserve the same check -- they are currently accepted and produce a negative speed.

## 2. Three of the six conversions in the in-program unit list are wrong

**Severity:** Medium
**Where:** `main.py` -> the `else` branch of the unit prompt

**What:** Entering an unrecognised unit prints a reference table. Three rows disagree with the constants the program calculates with:

    printed              constant           correct
    Half Marathons 21907.5m   HALF_MARATHON = 21097.5   21097.5
    Miles          1069.3m    MILES = 1609.344          1609.344
    Feet           0.38m      1 / FT (3.281)            0.3048

The half-marathon and mile figures are digit transpositions of the correct values; the foot figure is simply wrong. Marathons, kilometres, and metres are right.

**Why it matters:** The calculations are unaffected -- they use the constants -- so results are correct and only the reference is wrong, which is why this is Medium rather than High. But the table is printed precisely when a user is confused about units, so it is consulted at the moment they are least able to spot an error, and two of the three wrong values are transpositions that look plausible. Someone using it to sanity-check a distance elsewhere gets a mile 540 m short.

The root cause is that the constants and the printed table are two hand-maintained copies of the same six facts, twenty lines apart.

**Suggested fix:** Print the table from the constants rather than from literals -- a dict of unit name to metres, used by both the conversion branch and the help output. That removes the possibility of drift rather than correcting three instances of it.

## 3. The in-program licence notice is dated differently from the file header

**Severity:** Low
**Where:** `main.py` -> the `license` command; module docstring

**What:** The `license` command prints `Running Calculator Copyright (C) 2022-2023 @willtheorangeguy`. The module docstring at the top of the same file reads `Copyright (C) 2022-2026 willtheorangeguy`.

**Why it matters:** Small, and it is the one output whose job is stating the copyright accurately -- a user who types `license` is asking that exact question and gets an answer three years stale. The same pattern appears in `LEGO-Block-Creator` and `ProgramVer` in this sweep, which suggests the in-program notices across these projects were written once and never revisited.

**Suggested fix:** Derive both from one place, or at minimum update the command's string. Reading the year from `datetime` would stop it recurring.

---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
