#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from onion.area import calculate_demands

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def test_demands():

    population = 250000
    radius = 5 # km

    actual = calculate_demands(population, radius)
    expected = {'name': 'population_density',
                'value': 3183.0988618379065,
                'units': 'person/km^2'}

    assert actual == expected
