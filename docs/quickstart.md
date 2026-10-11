# Running Calculator — Quickstart

## Run it

```bash
git clone https://github.com/willtheorangeguy/Running-Calculator
cd Running-Calculator
python main.py
```

No dependencies.

## A run, start to finish

```text
What unit will you be inputting? miles
You are now entering in miles!

How far did you run? 3.1
How many hours did it take you? (if < 1, enter 0) 0
How many minutes did it take you? (if < 1, enter 0) 27
How many seconds did it take you? 14

You traveled 4.99 kilometers.
Your speed was 3.06 meters per second or 11.01 kilometers per hour.
```

Then it asks again, so you can do several runs without restarting.

## Units

`marathons`, `half marathons`, `miles`, `feet`, `kilometers`, `meters` — singular or plural,
case-insensitive, American spellings only. Full table in [Units](./units.md).

Anything else prints the unit list and asks again. Note three of the numbers in that printed list
are wrong; [Units](./units.md) has the correct ones.

## Do not enter zero for the whole time

```text
How many hours did it take you? 0
How many minutes did it take you? 0
How many seconds did it take you? 0
```

crashes with `ZeroDivisionError` — the speed is `distance / time` with nothing guarding a zero
total. The prompts explicitly suggest entering `0`, so it is easy to do while trying the program
out. Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## Other commands

At the unit prompt:

| Input | Does |
|---|---|
| `license` | Prints the licence notice |
| `quit`, `exit` | Leaves |

## Output is metric

Whatever you enter, results come back in metres or kilometres, and speeds in m/s and km/h. The
program says so on startup.
