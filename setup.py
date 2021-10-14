from setuptools import setup, find_packages
reqs = ['numpy', 'pandas', 'pathlib']

setup(
        name                  = "FieldSpecUtils",
        packages              = find_packages(),
        install_requires      = reqs,
        version               = "1.0.2",
        author                = "NERC Field Spectroscopy Facility",
        author_email          = "fsf@ed.ac.uk",
        description           = ("A software package for reading and processing data from Microtops II sun photometers, based on the package PyMicrotops by Robin Wilson"),
        license               = "MIT",
        url                   = "https://github.com/NERC-FSF/FieldSpectraUtils",
        classifiers           =[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2"
        ]
	)
		
