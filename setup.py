from codecs import open
from setuptools import setup

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

requires = []

setup(
    name='pytbo',
    version='0.0.2',
    description='Python Telegram Bots made easy',
    long_description=readme + '\n\n' + history,
    author='Alessandro Costa',
    author_email='alecosta.me@gmail.com',
    url='https://github.com/kostola/pytbo',
    packages=[ 'pytbo' ],
    install_requires=requires,
    license='Apache 2.0',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    )
)
