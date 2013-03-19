try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Wouter Oosterveld',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'wouter@fizzyflux.nl',
    'version': '0.1',
    'install_requires': ['nose','what','boto'],
    'packages': ['snaps'],
    'scripts': ['scripts/snaps'],
    'name': 'snaps'
}

setup(**config)
