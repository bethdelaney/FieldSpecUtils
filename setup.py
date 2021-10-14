import os
from setuptools import setup

PROJECT_ROOT = os.path.dirname(__file__)


def read_file(filepath, root=PROJECT_ROOT):
    """
    Return the contents of the specified `filepath`.
    * `root` is the base path and it defaults to the `PROJECT_ROOT` directory.
    * `filepath` should be a relative path, starting from `root`.
    """
    with open(os.path.join(root, filepath)) as fd:
        text = fd.read()
    return text

reqs = ['os', 'numpy', 'pandas', 'pathlib']

setup(
        name                  = "FieldSpectraUtils",
        packages              = ['FieldSpectraUtils'],
        install_requires      = reqs,
        version               = "1.0.0",
        author                = "NERC Field Spectroscopy Facility",
        author_email          = "fsf@ed.ac.uk",
        description           = ("A software package for reading and processing data from Microtops II sun photometers, based on the package PyMicrotops by Robin Wilson"),
        license               = "GNU General Public License v3.0",
        url                   = "https://github.com/NERC-FSF/FieldSpectraUtils",
        classifiers           =[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2"
        ]
	)
		