# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="Openfisca-CD93",
    version="1.0.1",
    description="Extension OpenFisca pour les aides sociales du conseil départemental de Seine Saint Denis",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="Incubateur de Services Numériques (SGMAP)",
    packages=find_packages(),
    install_requires=[
        'OpenFisca-Core >= 14, < 15',
        'OpenFisca-France >= 18, < 19'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
