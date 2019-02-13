#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from onion.area import calculate

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def test_population_density():

    population = 250000
    dwellings = 100000
    radius = 5 # km

    actual = calculate(population, dwellings, radius, None, None)
    expected = {
                'value': 3183.0988618379065,
                'units': 'person/km^2'
                }

    assert actual['population_density'] == expected

def test_substation_index(geojson):

    centroid = (-0.376931, 52.25207)
    buffer_km = 100

    population = 250000
    dwellings = 100000
    radius = 5 # km

    actual = calculate(population, dwellings, radius, centroid, geojson)
    expected = {
                'value':  -112.51793429649034,
                'units': ''
                }

    assert actual['substation_index'] == expected