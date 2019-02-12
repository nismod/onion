#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from onion.area import calculate_demands

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def test_demands():

    population = 250000
    radius = 1

    actual = calculate_demands(population, radius)
    expected = 10

    assert actual == expected