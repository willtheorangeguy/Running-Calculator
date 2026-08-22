<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Running-Calculator/logo.png" height="250px" width="400px" alt="Running Calculator">
  <br>
  Running Calculator
  <br>
</h1>

<!-- Copy -->
<h4 align="center">Work out your running speed from a distance and a time, in whatever unit you measured it.</h4>

<!-- Badges -->
<div align="center">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/Running-Calculator?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/Running-Calculator">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/Running-Calculator">
  <img alt="License" src="https://img.shields.io/github/license/willtheorangeguy/Running-Calculator">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot -->
<div align="center">
  <img alt="Running Calculator" src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Running-Calculator/welcome.png">
</div>

## Key Features

- Enter a distance in **marathons, half marathons, miles, feet, kilometres, or metres**.
- Enter a time in hours, minutes, and seconds.
- Get speed in metres per second and kilometres per hour.
- Loops, so you can do several runs in one sitting.
- Pure standard library; runs anywhere Python does.

Results are always metric, whatever you entered.

## Installation

```bash
git clone https://github.com/willtheorangeguy/Running-Calculator
cd Running-Calculator
python main.py
```

Also on PyPI and as a Docker image — see [`docs/installation.md`](docs/installation.md).

## Usage

```
What unit will you be inputting? miles
How far did you run? 3.1
How many hours did it take you? (if < 1, enter 0) 0
How many minutes did it take you? (if < 1, enter 0) 27
How many seconds did it take you? 14
```

Type `license` for the licence notice, or `quit` to leave.

> **Do not enter zero for all three time fields** — it divides by zero and exits with a traceback. See [`docs/internal/known-issues.md`](docs/internal/known-issues.md).

## Documentation

Full documentation lives in [`docs/`](docs/index.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Units](docs/units.md) · [Architecture](docs/architecture.md) · [Development](docs/development.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/Running-Calculator/discussions) or file an [issue](https://github.com/willtheorangeguy/Running-Calculator/issues/new/choose).

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/Running-Calculator/compare).

See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

This software uses the following open source packages, projects, services or websites:

<!-- Credits Table -->
<table>
  <tr>
    <th align="center"><img src="https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F2107379463%2Ficons%2Fmonochrome_large.png?w=240&h=240&s=8a19bbc158996d098e2fb18310ba7f33" width="150" height="150" alt="GitHub"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png" width="150" height="150" alt="PSF"/></th>
    <th align="center"><img src="https://pyinstaller.readthedocs.io/en/v4.2/_static/pyinstaller-draft1a.ico" width="150" height="150" alt="PyInstaller"/></th>
    <th align="center"><img src="https://pbs.twimg.com/profile_images/912151274551885824/sjzD5vK9_400x400.jpg" width="150" height="150" alt="Carbon"/></th>
  </tr>
  <tr>
    <td align="center">GitHub</td>
    <td align="center">Python Software Foundation</td>
    <td align="center">PyInstaller</td>
    <td align="center">Carbon</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/">Web</a> - <a href="https://github.com/pricing">Plans</a></td>
    <td align="center"><a href="https://www.python.org/">Web</a> - <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2">Donate</a></td>
    <td align="center"><a href="https://pyinstaller.readthedocs.io/en/stable/">Web</a> - <a href="https://www.pyinstaller.org/funding.html#funding-by-individuals">Donate</a></td>
    <td align="center"><a href="https://carbon.now.sh/">Web</a></td>
  </tr>
</table>

Sponsor [@willtheorangeguy](https://github.com/willtheorangeguy) on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US).

## License

MIT — see [`LICENSE.md`](LICENSE.md).
