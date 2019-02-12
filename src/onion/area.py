#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import argparse
import sys
import logging
from math import pi
from onion import __version__

__author__ = "Will Usher"
__copyright__ = "Will Usher"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def calculate_demands(population, radius):

    area = pi * radius**2
    density = population / area
    return density


def compute_ev_ownership(ev_power):

    return number_evs

def compute_ev_power(population):

    return ev_power_requirements


def compute_heating_demand(population, dwellings):

    pass


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a Fibonnaci demonstration")
    parser.add_argument(
        '--version',
        action='version',
        version='onion {ver}'.format(ver=__version__))
    parser.add_argument(
        dest="population",
        help="population",
        type=float,
        metavar="INT")
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)

    calculate_demands(args.population)



def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
