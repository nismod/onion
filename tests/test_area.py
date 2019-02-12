#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from onion.area import calculate

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def test_demands():

    population = 250000
    dwellings = 100000
    radius = 5 # km

    actual = calculate(population, dwellings, radius)
    expected = {
                'value': 3183.0988618379065,
                'units': 'person/km^2'
                }

    assert actual['population_density'] == expected
