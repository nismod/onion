=====
onion
=====

.. image:: https://travis-ci.com/nismod/onion.svg?branch=master
    :target: https://travis-ci.com/nismod/onion

Observation of new infrastructure operations and networks


Getting Started
===============

    pip install -e git+https://github.com/nismod/onion#egg=onion

    >>> from onion.area import run
    >>> population = 250000
    >>> dwellings = 100000
    >>> radius = 3.5
    >>> calculate(population, dwellings, radius)
    {'name': 'population_density', 'value': 6496.12012619981, 'units': 'person/km^2'}


Alternatively, clone and install the development version of the code

    git clone https://github.com/nismod/onion.git
    cd onion
    python setup.py develop
    