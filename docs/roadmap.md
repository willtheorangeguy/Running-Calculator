# Running Calculator — Roadmap

Direction, not a schedule. Defects are in
[`internal/known-issues.md`](./internal/known-issues.md).

## Where it is

Converts six distance units and a time into speed in m/s and km/h, loops for successive runs, and
validates numeric input. Two helper functions are separated out and tested.

## Considered

**Guarding zero time.** The one crash in the program, and the prompts invite the input that
causes it.

**Printing the unit table from the constants.** The table and the constants are two hand-kept
copies of the same six facts, and three have drifted. Deriving one from the other makes the class
of bug impossible rather than fixing three instances of it.

**Pace as well as speed.** Minutes per kilometre or mile is how runners actually talk about this,
and it is the same arithmetic inverted.

**Imperial output.** The startup message apologises for metric-only, which suggests it was always
meant to be optional.

**Range checking.** Negative distances and times are accepted and produce negative speeds.

**Command-line arguments.** Interactive-only means it cannot be scripted or piped.

## Non-goals

**GPS, watches, or file import.** Reading a track file or a watch export is a different program.
This takes two numbers.

**Storing runs.** A training log needs somewhere to keep data and something to show over time.
This answers one question and exits.

**Predicting race times.** Well served elsewhere, and a prediction presented next to a measurement
invites confusing the two.

**Guessing the unit.** The program takes your word for what you entered rather than inferring from
magnitude. A 5 that means kilometres and a 5 that means miles are both plausible, and guessing
wrong would be silent.

## Contributing

Issues and pull requests welcome — see the
[Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md).

The zero-time guard is two lines and removes the only way to crash it.
