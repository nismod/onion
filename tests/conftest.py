#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for onion.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest

@pytest.fixture()
def geojson():
    data = {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "operating_voltage": "400kV",
            "name": "MOULSFORD DOWN 400KV SUBSTATION"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [-1.16028744986759, 51.5351050684567]
        }
    }, {
        "type": "Feature",
        "properties": {
            "operating_voltage": "400kV",
            "name": "CULHAM JET 400KV SUBSTATION"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [-1.22835338989177,
                51.6611686319984
            ]
        }
    }, {
        "type": "Feature",
        "properties": {
            "operating_voltage": "400kV",
            "name": "DIDCOT 400KV SUBSTATION"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [-1.25934538640586, 51.6255544962863]
        }
    }]
    }
    return data
