from setuptools import setup, find_packages


APP_NAME = 'ngsdb'
VERSION = '0.1.0'
AUTHOR = 'James Hibbard'

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    description="ngsdb",
    license="MIT",
    install_requires=[
        'Click==7.0',
        'Flask==1.0.2',
        'SQLAlchemy==1.3.1',
        'psycopg2-binary==2.7.7',
    ],
    extras_require={
        'migrate': ['alembic==1.0.8'],
        'test': ['pytest==4.3.1'],
        'doc': ['Sphinx==1.8.5'],
        'examples': ['jupyterlab-0.35.4'],
        'reflect': ['sqlacodegen==2.0.1'],
    },
    # The keys to this dictionary are package names, and an empty package name
    # stands for the root package.
    package_dir={'ngsdb': 'src'},
    # find_packages() walks the target directory (package dir: src), filtering
    # by inclusion patterns, and finds Python packages (any directory).
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        ngsdb=ngsdb.runner:cli
    ''',
)
