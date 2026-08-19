# Running Calculator — FAQ

### It crashed when I entered zero for the time.

`ZeroDivisionError` — the speed is `distance / time` with no guard against a total of zero. The
prompts suggest entering `0` for hours and minutes, so it is easy to reach by entering `0` for
all three while trying it out.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

### The unit list shows different numbers from the documentation.

The documentation is right. Three rows of the in-program list are wrong — half marathons, miles,
and feet — while the constants the program actually calculates with are correct.

So your results are fine; the printed reference is not. See [Units](./units.md).

### Why is the output always metric?

By design, and the program says so on startup. Distances come back in metres or kilometres, and
speeds in m/s and km/h, whatever you entered.

### Can I get my pace instead of my speed?

No — minutes per kilometre or mile is not calculated. See [Roadmap](./roadmap.md).

### `kilometres` is not recognised.

Only American spellings. Singular and plural both work, and case does not matter.

### Can I enter a negative distance or time?

It will accept them and produce a negative speed. There is no range checking.

### Does it remember previous runs?

No. Nothing is written to disk. The loop lets you do several in one sitting, and they are gone
when you exit.

### How accurate are the conversions?

The marathon and half-marathon figures are exact by definition, and the mile is the international
mile. The foot is derived as `1 / 3.281`, which gives 0.30479 rather than the defined 0.3048 — a
difference of about 3 mm per kilometre, invisible at running distances.

### How do I quit?

Type `quit` or `exit` at the unit prompt. They are not accepted during the time prompts.

### What does `license` do?

Prints the licence notice. Note it says 2022-2023 while the file header says 2022-2026.
