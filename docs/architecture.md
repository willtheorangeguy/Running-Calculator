# Running Calculator — Architecture

One file, 203 lines, three functions.

```text
main()
 ├── unit prompt        →  a chain of elif comparisons setting `unit`
 ├── time prompts       →  float/int, wrapped in try/except ValueError
 ├── conversion         →  everything to metres and seconds
 ├── calculate_distance →  metres or kilometres for display
 └── display_result     →  the output
```

## `main()`

Two nested loops: an outer `while run` for successive runs, and inner loops for the unit and the
time entry. Both inner flags are reset at the bottom so the next run starts clean.

The unit prompt is a chain of `elif` comparisons against lowercased input, accepting singular and
plural. `license`, `quit`, and `exit` are handled in the same chain — which is why they are only
available at that prompt and not during time entry.

## Input validation

```python
try:
    time_run = False
    length = float(input("How far did you run? "))
    hours = int(input(...))
    ...
except ValueError:
    print("Values must be in numerical form, and only seconds can be a decimal!")
    time_run = True
```

Catching `ValueError` and re-prompting is right, and the message correctly explains that only
seconds may be fractional — `hours` and `mins` are parsed with `int`.

What is not guarded is a **total time of zero**, which reaches `distance / time` and raises
`ZeroDivisionError`. Negative values are also accepted, producing a negative speed. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Conversion

Constants at the top of `main()`:

```python
FT = 3.281
MILES = 1609.344
HALF_MARATHON = 21097.5
MARATHON = 42195
```

Each unit multiplies (or, for feet, divides) into metres. These values are correct — unlike the
reference table printed on unrecognised input, which disagrees with three of them. See
[Units](./units.md).

## `calculate_distance(distance, unit)`

Returns metres below 1,000 and kilometres above, overwriting the `unit` argument it was passed.
Purely for display; the speed is computed from the metre value before this is called.

## `display_result(...)`

Prints the distance and both speeds, rounded to two places.

## What is absent

No pace (minutes per kilometre or mile), no imperial output, no history, no persistence, and no
argument parsing — the program is interactive only. See [Roadmap](./roadmap.md).
