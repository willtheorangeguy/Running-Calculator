# Running Calculator — Units

## Accepted at the unit prompt

Singular and plural both work, and matching is case-insensitive.

| Input | Also accepted |
|---|---|
| `marathons` | `marathon` |
| `half marathons` | `half marathon` |
| `miles` | `mile` |
| `feet` | `foot` |
| `kilometers` | `kilometer` |
| `meters` | `meter` |

American spellings only — `kilometres` and `metres` are not recognised.

## The conversions the program uses

These are the constants in `main.py`, and they are correct:

| Unit | Metres |
|---|---|
| Marathon | 42,195 |
| Half marathon | 21,097.5 |
| Mile | 1,609.344 |
| Foot | 0.3048 (as `1 / 3.281`) |
| Kilometre | 1,000 |
| Metre | 1 |

A marathon is 42.195 km by definition, and a half marathon exactly half of it. The mile figure is
the international mile. The foot is derived by dividing by 3.281 feet-per-metre, which gives
0.30479 — close enough to the defined 0.3048 that it will not show at running distances.

## The list the program prints is wrong

Entering an unrecognised unit prints a reference table, and three of its six rows disagree with
the constants above:

| Row | Printed | Correct |
|---|---|---|
| Half Marathons | 21907.5m | **21097.5m** — digits transposed |
| Miles | 1069.3m | **1609.344m** — digits transposed |
| Feet | 0.38m | **0.3048m** |
| Marathons | 42195m | Correct |
| Kilometers | 1000m | Correct |
| Meters | 1m | Correct |

**Your results are not affected** — the calculation uses the constants, not the printed table. But
anyone reading those numbers as a reference gets three wrong ones, and the two transpositions are
the kind that look plausible.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## Output units

Always metric:

- Distance in **metres** below 1,000, **kilometres** above.
- Speed in **metres per second** and **kilometres per hour**.

There is no imperial output, and no pace (minutes per kilometre or mile) — see
[Roadmap](./roadmap.md).
