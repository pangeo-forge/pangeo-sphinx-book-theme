# Pangeo Sphinx Book Theme

[![PyPI version](https://badge.fury.io/py/pangeo-sphinx-book-theme.svg)](https://badge.fury.io/py/pangeo-sphinx-book-theme)

This is a theme for [Sphinx](http://sphinx-doc.org/) that inherits from the
[Sphinx Book Theme](https://github.com/executablebooks/sphinx-book-theme).

It is used for the [Pangeo Forge documentation](https://pangeo-forge.readthedocs.io/en/latest/) and related projects.

## Build the documentation

This site comes bundled with a small documentation site to make it easy to preview what the theme looks like.

The easiest way to build the documentation is to us [the nox command line tool](https://nox.thea.codes/).
This is kind-of like a `Makefile` that is bundled with an isolated local environment.

To build the documentation with `nox`, run this command:

```
nox -s docs
```

To build the documentation with a live server that auto-reloads when you make changes to `docs/`, run this command:

```
nox -s docs-live
```

Configuration for `nox` can be found in `noxfile.py`.
