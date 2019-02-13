#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import argparse
import sys
from math import pi

from .indices import calculate_substation_index, calculate_road_index

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"


def calculate_population_density(population, radius):

    area = pi * radius**2  # sq km
    population_density = population / area
    return population_density

def calculate_dwelling_density(dwellings, radius):

    area = pi * radius**2  # sq km
    dwelling_density = dwellings / area
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

def estimate_pv_generation(total_roof_area):
    average_daylight_hours = 12
    pv_load_factor = 0.11
    capacity = estimate_solar_pv_potential(total_roof_area)
    return average_daylight_hours * pv_load_factor * capacity


def calc_heat_density(total_heat_demand, radius):
    area = pi * radius**2  # sq km
    return total_heat_demand / area


def heat_network(total_heat_demand, radius):
    heat_density = calc_heat_density(total_heat_demand, radius)
    if heat_density > 50:
        heat_network_capacity = total_heat_demand
    else:
        heat_network_capacity = 0

    return heat_network_capacity

def heat_pumps(dwellings, dwelling_density):

    if dwelling_density > 100:
        return 0
    elif dwelling_density > 50 and dwelling_density <= 100:
        return dwellings * 1360 / 2
    elif dwelling_density <= 50:
        return dwellings * 1360 / 2.5


def compute_space_heating_demand(dwellings, population, proportion_evs=0.6, scenario='existing'):

    # exiting
    if scenario == 'existing':
        heating_demand = dwellings * 8000  # kWh/year
        hot_water = dwellings * 5000  # kWh/year
        electricity = dwellings * 3000  # kWh/year
    # zero carbon
    elif scenario == 'zero_carbon':
        heating_demand = dwellings * 1360  # kWh/year
        hot_water = dwellings * 5000  # kWh/year
        electricity = dwellings * 2700  # kWh/year    

    ev_electricity = dwellings * proportion_evs * 2000

    return {'space_heat': heating_demand,
            'hot_water': hot_water,
            'electricity': electricity,
            'ev_electricity': ev_electricity,
            'total_electricity': electricity + ev_electricity,
            'total_heat': heating_demand + hot_water}


def calculate(population, dwellings, radius_km,
              centroid, feature_geojson):
    """

    Arguments
    ---------
    population : int
        The population count of the city circle
    dwellings : int
        The dwelling count of the city circle
    radius_km : int
        The radius in kilometres of the city circle
    centroid : tuple of int
        The lon/lat pair for the centre of the city circle
    feature_geojson : dict
        A geojson dict of substation data
    """

    results = {}

    av_roof_area = 25  # m^2
    av_floor_area = 55  # m^2

    population_density = calculate_population_density(population, radius_km)
    dwelling_density = calculate_dwelling_density(dwellings, radius_km)
    total_roof_area = estimate_roof_area(dwellings, av_roof_area)
    pv_potential = estimate_solar_pv_potential(total_roof_area)
    total_floor_area = estimate_floor_area(dwellings, dwelling_density, 
                                           av_floor_area)

    energy_demand = compute_space_heating_demand(dwellings, population, 
                                                 proportion_evs=0.6,
                                                 scenario='existing')

    heat_network_energy = heat_network(energy_demand['total_heat'], radius_km)
    
    energy_supply_shortfall_elec = energy_demand['total_electricity'] - pv_potential
    energy_supply_shortfall_heat = energy_demand['total_heat'] - heat_network_energy



    results = {
        'population_density': {'value': round(population_density), 'units': 'person/km^2'},
        'dwelling_density': {'value': round(dwelling_density), 'units': 'dwelling/hectare'},
        'energy_supply_solar_pv_potential': {'value': round(pv_potential, 2), 'units': 'kWh'},
        'energy_supply_heat_network_potential': {'value': round(heat_network_energy, 2), 'units': 'kWh'},
        'energy_supply_heat_pump_potential': {'value': round(heat_pumps(dwellings, dwelling_density), 2), 'units': 'kWh'},
        'energy_demand_space_heat': {'value': round(energy_demand['space_heat'], 2), 'units': 'kWh/year'},
        'energy_demand_hot_water': {'value': round(energy_demand['hot_water'], 2), 'units': 'kWh/year'},
        'energy_demand_electricity': {'value': round(energy_demand['electricity'], 2), 'units': 'kWh/year'},
        'energy_demand_ev_electricity': {'value': round(energy_demand['ev_electricity'], 2), 'units': 'kWh/year'},
        'total_floor_area': {'value': round(total_floor_area), 'units': 'm^2'}
    }

    if feature_geojson:
        substation_index = calculate_substation_index(centroid,
                                                      feature_geojson,
                                                      radius_km)
        results['substation_index'] = {'value': substation_index, 'units': ""}

        road_index = calculate_road_index(feature_geojson)
        results['congestion_index'] = {'value': road_index,
                                       'units': ''}

    return results


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
