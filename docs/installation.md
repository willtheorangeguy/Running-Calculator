# Running Calculator — Installation

## Requirements

Python 3.x. No dependencies.

## From source

```bash
git clone https://github.com/willtheorangeguy/Running-Calculator
cd Running-Calculator
python main.py
```

## From PyPI

```bash
pip install running-calculator
running-calculator
```

## Docker

```bash
docker pull ghcr.io/willtheorangeguy/running-calculator:main
docker run -i -t ghcr.io/willtheorangeguy/running-calculator:main
```

Interactive mode matters — the program is a series of prompts, so `-i -t` is required.

## Verify

```bash
python main.py
```

You should get the ASCII runner, the banner, and the unit prompt. Type `quit` to leave.

## Uninstall

```bash
pip uninstall running-calculator
```

Nothing is written to disk — no config, no history, no saved runs.
