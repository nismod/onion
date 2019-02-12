#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import argparse
import sys
from math import pi
import pandas as pd
from onion import __version__

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def calculate_population_density(population, radius):

    area = pi * radius**2
    population_density = population / area
    return population_density


def dwelling_density(dwellings, radius):

    area = pi * radius**2
    dwelling_density = dwellings / area
    return dwelling_density


def estimate_floor_area(dwellings, dwelling_density):

    return floor_area


def compute_ev_ownership(ev_power):

    return number_evs

def compute_ev_power(population):

    

    return ev_power_requirements


def compute_heating_demand(population, dwellings):

    pass



def calculate(population, radius):

    population_density = calculate_population_density(population, radius)
    return {'name': 'population_density',
            'value': population_density,
            'units': 'person/km^2'}


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Observation of new infrastructure operations and networks")
    parser.add_argument(
        '--version',
        action='version',
        version='onion {ver}'.format(ver=__version__))
    parser.add_argument(
        dest="population",
        help="population",
        type=float,
        metavar="INT")
    parser.add_argument(
        dest="radius",
        help="radius (in km)",
        type=float,
        metavar="INT")
    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    print(calculate_demands(args.population, args.radius))



def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
