from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Python module depending on matplotlib to draw oak leaf.'
LONG_DESCRIPTION = 'Python module depending on matplotlib and angle to draw oak leaf wih specific title.'

setup(
    name="python-oak-leaf-drawer",
    version="1.0.0",
    author="Karam Mustafa",
    author_email="karam2mustafa@gmail.com",
    description="Python module depending on matplotlib to draw oak leaf.",
    long_description_content_type="Python module depending on matplotlib and angle to draw oak leaf wih specific title.",
    long_description="Python module depending on matplotlib and angle to draw oak leaf wih specific title.",
    packages=find_packages(),
    install_requires=['matplotlib'],
    keywords=['python', 'oak', 'oak-leaf', 'python-packages', 'matplotib'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)