# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the app:**
```bash
python main.py
# or, if installed as a package:
running-calculator
```

**Run all tests:**
```bash
pytest
```

**Run a single test:**
```bash
pytest tests/test_main.py::test_calculate_distance
pytest tests/test_main.py::test_display_result
```

**Lint:**
```bash
pylint $(git ls-files '*.py')
```

**Build the package:**
```bash
python -m build
```

**Run via Docker:**
```bash
docker-compose up
```

## Architecture

This is a single-file procedural CLI app. All logic lives in `main.py`; `__main__.py` is just a thin wrapper that calls `main()`.

**Data flow in `main()`:**
1. User selects a unit (marathons, half-marathons, miles, feet, kilometers, meters)
2. User enters distance and elapsed time (hours/minutes/seconds)
3. Input is converted to raw meters using constants (`MARATHON=42195`, `HALF_MARATHON=21097.5`, `MILES=1609.344`, `FT=3.281`)
4. Speed is calculated in m/s and km/h
5. `calculate_distance()` decides whether to display in meters or kilometers (>1000 m → km)
6. `display_result()` prints the formatted output
7. The loop resets `length_run = True` / `time_run = True` and repeats from step 1

`main()` contains the full interactive loop including special commands (`license`, `quit`/`exit`) and all input validation — it is not unit-tested because it relies on `input()`. Only `calculate_distance` and `display_result` have tests.

## Conventions

- **Indentation:** 4 spaces, never tabs
- **Naming:** `snake_case` for functions, `UPPER_SNAKE_CASE` for constants (no classes exist yet)
- **Pylint suppressions:** `main.py` suppresses `invalid-name`, `too-many-locals`, `too-many-branches`, `too-many-statements` at the file level — keep this header when editing that file
- **Comments:** Code is expected to be heavily commented per `CONTRIBUTING.md`
- **Versioning:** Semantic Versioning; update `pyproject.toml` and `setup.cfg` together when bumping versions
- **Branch workflow:** GitHub Flow — branch off `main`, open a PR

## Known Issues

- `setup.cfg` has a typo in the entry point: `runnning-calculator` (three n's) vs the correct `running-calculator` in `setup.py`
- The help text in `main()` shows `Miles = 1069.3m` and `Feet = 0.38m`, which are inconsistent with the actual constants used in the calculation (`MILES=1609.344`, `FT=3.281`)
