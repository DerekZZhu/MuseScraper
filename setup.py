from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.1"
DESCRIPTION = "A library for mass scraping Musescore.com"

# Set up
setup(
    name="musescraper",
    version=VERSION,
    author="Rek505 (Derek Zhu)",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests", "urllib.request", "requests_html"],
    keywords=['webscraping', 'musescore', 'automation']
)
