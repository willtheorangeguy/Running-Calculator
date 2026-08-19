# Running Calculator — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/Running-Calculator
cd Running-Calculator
pip install -r requirements.txt
python main.py
```

No runtime dependencies.

## Tests

```bash
pytest
```

`tests/` covers the calculation and display helpers. `calculate_distance` and `display_result`
are separate functions precisely so they can be tested without driving the prompts — keep that
split.

`main()` itself is one long interactive loop and is not directly testable. Anything new worth
asserting should go in a function outside it.

## Where the known issues live

Both are in `main()`:

- **`metersps = distance / time`** with no zero guard.
- **The unit list printed on unrecognised input**, whose half-marathon, mile, and foot values
  disagree with the constants a few lines below.

The second is the more interesting one to fix properly: the constants and the printed table are
two hand-maintained copies of the same facts, which is why they drifted. Printing the table from
the constants would make it impossible.

## Conventions

- **Module docstring and copyright header** on every file.
- **Pylint**, with per-file disables at the top.
- Standard library only.
- **American unit spellings** in the input matching.

## The licence notice

The in-program `license` command prints `Copyright (C) 2022-2023`, while the module header says
2022-2026. Worth reading from one place if either is ever updated.

## Recording defects

Bugs found while working here go in [`internal/known-issues.md`](./internal/known-issues.md)
rather than being fixed in passing, unless fixing them is the job you are on.
