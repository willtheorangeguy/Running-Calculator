# Running Calculator — Documentation

Converts a distance and a time into a speed, from the command line.

```
Running-Calculator/
├── main.py    the whole program: prompts, conversion, output
└── docs/      this documentation
```

## Pages

- [Quickstart](./quickstart.md) — one run, start to finish
- [Installation](./installation.md) — source, PyPI, Docker
- [Units](./units.md) — what each unit converts to
- [Architecture](./architecture.md) — the three functions
- [Development](./development.md) — tests and conventions
- [FAQ](./faq.md) — metric output, accepted units, the loop
- [Troubleshooting](./troubleshooting.md) — the crash, and unrecognised units
- [Roadmap](./roadmap.md) — direction and non-goals
- [Known issues](./internal/known-issues.md) — recorded defects

## Two things to know

**Zero time crashes it.** The speed is `distance / time` with no guard, so entering 0 hours, 0
minutes, and 0 seconds exits with a `ZeroDivisionError` traceback. The prompts invite zeros —
"(if < 1, enter 0)" — which makes it easy to hit while exploring.

**The in-program unit list has wrong numbers.** Typing an unrecognised unit prints a reference
table, and three of its six values are wrong. The conversions the program *uses* are correct, so
your results are right; the reference is not. See [Units](./units.md) for the correct figures.

Both in [`internal/known-issues.md`](./internal/known-issues.md).

## What it does

1. Asks which unit you are entering.
2. Asks the distance, then hours, minutes, and seconds.
3. Converts everything to metres and seconds.
4. Prints the distance (in metres or kilometres) and the speed in m/s and km/h.
5. Loops for another run.

Output is always metric, whatever you entered — the program says so on startup.

## Extra commands

At the unit prompt:

| Input | Does |
|---|---|
| `license` | Prints the licence notice |
| `quit` or `exit` | Leaves |
| Anything unrecognised | Prints the unit list and asks again |
