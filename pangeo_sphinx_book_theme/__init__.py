"""Pangeo Sphinx Book Theme.
"""
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from os import path

def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir

def set_theme_defaults(app):
    if not app.config.html_logo:
        app.config.html_logo = "pangeo-logo.png"

# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('pangeo_sphinx_book_theme', path.abspath(path.dirname(__file__)))
    app.connect("builder-inited", set_theme_defaults)
