=====
onion
=====


Observation of new infrastructure operations and networks


Getting Started
===============

    pip install -e git+https://github.com/nismod/onion#egg=onion

    >>> from onion.area import run
    >>> population = 250000
    >>> radius = 3.5
    >>> run(population, radius)
    {'name': 'population_density', 'value': 6496.12012619981, 'units': 'person/km^2'}

