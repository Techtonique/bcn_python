

# BCN | <a class="github-button" href="https://github.com/Techtonique/bcn_python/stargazers" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" aria-label="Star BCN/BCN on GitHub">Star</a>

![PyPI](https://img.shields.io/pypi/v/BCN) [![PyPI - License](https://img.shields.io/pypi/l/BCN)](https://github.com/Techtonique/bcn_python/blob/main/LICENSE) [![Downloads](https://pepy.tech/badge/BCN)](https://pepy.tech/project/BCN) [![Last Commit](https://img.shields.io/github/last-commit/Techtonique/bcn_python)](https://github.com/Techtonique/bcn_python)

Welcome to __BCN__'s website.

This package contains an implementation of **Boosted Configuration (*neural*) Networks** (BCNs). How do BCNs work? By creating ensembles (boosting in a supervised way) of single-layered feedforward (*neural*) Networks.

It's worth mentioning that the Python package is built on top of the [`R package`](https://techtonique.r-universe.dev/ui#package:bcn), thanks to `rpy2`.

__BCN__’s source code is [available on GitHub](https://github.com/Techtonique/bcn_python). 

Looking for a specific function? You can also use the __search__ function available in the navigation bar.

## Installing

- __1st method__: by using `pip` at the command line for the stable version

```bash
pip install BCN
```

- __2nd method__: from Github, for the development version

```bash
pip install git+https://github.com/Techtonique/bcn_python.git
```

or 

```bash
git clone https://github.com/Techtonique/bcn_python.git
cd BCN
make install
```

## Quickstart 

Examples of use: 

- For [classification](examples/classification.md)

- For [regression](examples/regression.md)

## Documentation

The documentation for each model can be found (work in progress) here:

- For the [classifier](documentation/classifier.md)

- For the [regressor](documentation/regressor.md)

<script async defer src="https://buttons.github.io/buttons.js"></script>