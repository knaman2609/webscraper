from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='webscraper',
    version='0.0',
    description='webscraper',
    author='Naman Kalkhuria',
    author_email='naman.kalkhuria1@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
