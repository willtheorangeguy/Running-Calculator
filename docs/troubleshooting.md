# Running Calculator — Troubleshooting

## `ZeroDivisionError: float division by zero`

You entered zero for hours, minutes, and seconds. The speed calculation has no guard for a total
time of zero.

Enter the real time. If you genuinely want to check the behaviour, one second is enough.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## "Please try again. Options are:" when I typed a real unit

Only these are recognised, in American spelling:

`marathons`, `half marathons`, `miles`, `feet`, `kilometers`, `meters` — singular or plural.

The British spellings are not, and neither are abbreviations like `km`, `mi`, or `ft`.

## The unit list numbers look wrong

They are, for three of the six rows. [Units](./units.md) has the correct figures. Your
calculations are unaffected — the program uses its constants, not the printed list.

## "Values must be in numerical form"

Hours and minutes are parsed as integers; only seconds may have a decimal point. `1.5` hours is
rejected — enter `1` hour and `30` minutes.

All four values are re-prompted after this error, not just the bad one.

## `quit` does not work

It is only recognised at the unit prompt. Once you are entering distance and time, finish the
entry or interrupt with Ctrl+C.

## The speed looks far too high or low

Check the unit you selected. Entering a marathon distance while in `meters` mode gives a very
different answer from `marathons` mode — the program takes your word for the unit.

## Nothing happens in Docker

The program is interactive, so the container needs a TTY:

```bash
docker run -i -t ghcr.io/willtheorangeguy/running-calculator:main
```

## The ASCII art is mangled

A terminal narrower than the banner, or one without UTF-8. Cosmetic.

## Still stuck

[Open an issue](https://github.com/willtheorangeguy/Running-Calculator/issues/new/choose) with
what you entered and what came back.
