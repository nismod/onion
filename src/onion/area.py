#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import argparse
import sys
from math import pi
import pandas as pd

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def calculate_population_density(population, radius):

    area = pi * radius**2  # sq km
    population_density = population / area  
    return population_density


def calculate_dwelling_density(dwellings, radius):

    area = pi * radius**2  # sq km
    area_hectares = area * 100.0
    dwelling_density = dwellings / area_hectares
    return dwelling_density


def estimate_floor_area(dwellings, dwelling_density, floor_area):

    total_floor_area = dwellings * floor_area

    return total_floor_area

def estimate_roof_area(dwellings, roof_area):

    total_roof_area = dwellings * roof_area

    return total_roof_area

def estimate_solar_pv_potential(total_roof_area):

    KWp_PER_SQ_M = 0.12
    pv_potential = total_roof_area * KWp_PER_SQ_M
    return pv_potential


def compute_ev_ownership(ev_power):

    return number_evs

def compute_ev_power(population):

    return ev_power_requirements


def compute_heating_demand(population, dwellings):

    pass



def calculate(population, dwellings, radius):

    av_roof_area = 25  # m^2
    av_floor_area = 55  # m^2

    population_density = calculate_population_density(population, radius)
    dwelling_density = calculate_dwelling_density(dwellings, radius)
    total_roof_area = estimate_roof_area(dwellings, av_roof_area)
    pv_potential = estimate_solar_pv_potential(total_roof_area)
    total_floor_area = estimate_floor_area(dwellings, dwelling_density, av_floor_area)

    return {'population_density': {'value': population_density, 'units': 'person/km^2'},
            'dwelling_density': {'value': dwelling_density, 'units': 'dwelling/hectare'},
            'solar_pv_potential': {'value': pv_potential, 'units': 'kWp'},
            'floor_area': {'value': total_floor_area, 'units': 'm^2'}
            }


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
