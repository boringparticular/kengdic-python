import os
import sys
from setuptools import setup

install_requires = [
    "future",
]

test_requires = ["nose2", "coverage", "coveralls"]

if sys.version_info[:2] < (3, 5):
    raise RuntimeError("Python version >=3.5 required.")

version_py = os.path.join(os.path.dirname(__file__), "kengdic", "version.py")
version = open(version_py).read().strip().split("=")[-1].replace('"', "").strip()

setup(
    name="kengdic",
    version=version,
    description="kengdic",
    author="Scott Gigante",
    author_email="scott.gigante@yale.edu",
    packages=[
        "kengdic",
    ],
    include_package_data=True,
    license="Mozilla Public License Version 2.0",
    install_requires=install_requires,
    extras_require={"test": test_requires},
    test_suite="nose2.collector.collector",
    url="https://github.com/scottgigante/kengdic",
    download_url="https://github.com/scottgigante/kengdic/archive/v{}.tar.gz".format(
        version
    ),
    keywords=[
        "korean",
        "english",
        "dictionary",
        "translation",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Jupyter",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Natural Language :: Korean",
        "Programming Language :: SQL",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Education",
    ],
)
