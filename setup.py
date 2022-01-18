# -*- coding: utf-8 -*-
"""`pangeo-sphinx-book-theme` lives on `Github`_.

.. _github: https://github.com/pangeo-forge/pangeo-sphinx-book-theme/

"""
from io import open
from setuptools import setup
import versioneer

setup(
    name='pangeo_sphinx_book_theme',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/pangeo-forge/pangeo-sphinx-book-theme/',
    license='MIT',
    author='Ryan Abernathey',
    author_email='rpa@ldeo.columbia.edu',
    maintainer='Charles Stern',
    maintainer_email='cstern@ldeo.columbia.edu',
    description='Pangeo\'s customized version of the Sphinx Book Theme.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=['pangeo_sphinx_book_theme'],
    package_data={'pangeo_sphinx_book_theme': [
        'theme.conf',
        '*.html',
        'static/*.css',
        'static/*.otf',
        'static/*.png'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'pangeo_sphinx_book_theme = pangeo_sphinx_book_theme',
        ]
    },
    install_requires=[
       'sphinx', 'sphinx_book_theme<=0.1.7'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
