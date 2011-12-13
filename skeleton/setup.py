try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'My Name',
        'url': 'url to get in at',
        'download_url': 'where to download it.',
        'author_email': 'My email.',
        'verson': '0.1',
        'install_requirse': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)
