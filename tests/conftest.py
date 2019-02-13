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
def geojson_no_substation():
    data = \
        {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "type": "railwaystation",
                        "code": "APF",
                        "pax": 6562
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            -1.24262902639089,
                            51.6389953266527
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {
                        "type": "railwaystation",
                        "code": "CHO",
                        "pax": 271850
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            -1.15824245298617,
                            51.5700313809884
                        ]
                    }
                }
            ]
         }
    return data

@pytest.fixture()
def geojson():
    data = \
    {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "type": "substation",
                "operating_voltage": "400kV",
                "name": "MOULSFORD DOWN 400KV SUBSTATION"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.16028744986759,
                    51.5351050684567
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "substation",
                "operating_voltage": "400kV",
                "name": "CULHAM JET 400KV SUBSTATION"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.22835338989177,
                    51.6611686319984
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "substation",
                "operating_voltage": "400kV",
                "name": "DIDCOT 400KV SUBSTATION"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.25934538640586,
                    51.6255544962863
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "railwaystation",
                "code": "APF",
                "pax": 6562
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.24262902639089,
                    51.6389953266527
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "railwaystation",
                "code": "CHO",
                "pax": 271850
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.15824245298617,
                    51.5700313809884
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "railwaystation",
                "code": "DID",
                "pax": 3185928
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.24252767003678,
                    51.6112380133509
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "railwaystation",
                "code": "RAD",
                "pax": 141792
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.24027394922877,
                    51.6856723771796
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "railwaystation",
                "code": "CUM",
                "pax": 83908
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.23655176310231,
                    51.6541065120975
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A34",
                "traffic": 54439,
                "length": 4.6
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.31059706481581,
                            51.6689864665425
                        ],
                        [
                            -1.26781096387948,
                            51.6985339675415
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A329",
                "traffic": 3345,
                "length": 7.1
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.13794664310112,
                            51.6300105153004
                        ],
                        [
                            -1.13140405984907,
                            51.6813305265736
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 19149,
                "length": 3.2
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.30318526319598,
                            51.6185999321814
                        ],
                        [
                            -1.25803683722294,
                            51.6148526981605
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4074",
                "traffic": 17856,
                "length": 4.8
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.10356919925638,
                            51.5966013607872
                        ],
                        [
                            -1.13794664310112,
                            51.6300105153004
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A34",
                "traffic": 48111,
                "length": 6.2
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.29769415515151,
                            51.5719374629499
                        ],
                        [
                            -1.30318526319598,
                            51.6185999321814
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 14424,
                "length": 6.3
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.28106464112459,
                            51.670230120639
                        ],
                        [
                            -1.20964403885468,
                            51.656976647206
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4074",
                "traffic": 14875,
                "length": 2.1
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.17592127762952,
                            51.6591726282996
                        ],
                        [
                            -1.19173995500197,
                            51.6752692494828
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 10892,
                "length": 2.9
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.31049389680317,
                            51.5995272553624
                        ],
                        [
                            -1.30318526319598,
                            51.6185999321814
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 17857,
                "length": 0.3
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.28197758152293,
                            51.6728521889952
                        ],
                        [
                            -1.28106464112459,
                            51.670230120639
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 27740,
                "length": 1.8
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.31059706481581,
                            51.6689864665425
                        ],
                        [
                            -1.28543294417051,
                            51.6701488702853
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4074",
                "traffic": 17849,
                "length": 4.9
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.19173995500197,
                            51.6752692494828
                        ],
                        [
                            -1.22487138489146,
                            51.7134539721219
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4183",
                "traffic": 18705,
                "length": 1
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.27055101721002,
                            51.6900991535893
                        ],
                        [
                            -1.26781096387948,
                            51.6985339675415
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 9314,
                "length": 9.2
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.22783995884067,
                            51.6070152905303
                        ],
                        [
                            -1.12972742224083,
                            51.587626761905
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A329",
                "traffic": 6865,
                "length": 5.8
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.14706180031622,
                            51.5406380360533
                        ],
                        [
                            -1.12972742224083,
                            51.587626761905
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 7587,
                "length": 2.5
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.20964403885468,
                            51.656976647206
                        ],
                        [
                            -1.17592127762952,
                            51.6591726282996
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4185",
                "traffic": 10001,
                "length": 3.4
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.29769415515151,
                            51.5719374629499
                        ],
                        [
                            -1.31049389680317,
                            51.5995272553624
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A417",
                "traffic": 11512,
                "length": 7.2
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.41043567263547,
                            51.5903607602834
                        ],
                        [
                            -1.31049389680317,
                            51.5995272553624
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A34",
                "traffic": 58188,
                "length": 5.9
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.30318526319598,
                            51.6185999321814
                        ],
                        [
                            -1.31059706481581,
                            51.6689864665425
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 12092,
                "length": 3.8
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.36284412567133,
                            51.6697759046812
                        ],
                        [
                            -1.31059706481581,
                            51.6689864665425
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A417",
                "traffic": 4443,
                "length": 13.5
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.31049389680317,
                            51.5995272553624
                        ],
                        [
                            -1.15736123969025,
                            51.5372956161098
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4074",
                "traffic": 18534,
                "length": 4.3
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.13794664310112,
                            51.6300105153004
                        ],
                        [
                            -1.17592127762952,
                            51.6591726282996
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 14810,
                "length": 0.3
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.28543294417051,
                            51.6701488702853
                        ],
                        [
                            -1.28106464112459,
                            51.670230120639
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A34",
                "traffic": 45394,
                "length": 2.1
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.29826497644884,
                            51.553598176905
                        ],
                        [
                            -1.29769415515151,
                            51.5719374629499
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A417",
                "traffic": 4443,
                "length": 1.5
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.15736123969025,
                            51.5372956161098
                        ],
                        [
                            -1.14922261884273,
                            51.5252780221871
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4185",
                "traffic": 10001,
                "length": 0.1
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.29769415515151,
                            51.5719374629499
                        ],
                        [
                            -1.29639842872763,
                            51.5717498749626
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4183",
                "traffic": 10570,
                "length": 2.2
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.28197758152293,
                            51.6728521889952
                        ],
                        [
                            -1.27055101721002,
                            51.6900991535893
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 10338,
                "length": 0.9
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.22783995884067,
                            51.6070152905303
                        ],
                        [
                            -1.22435490208312,
                            51.6140866024406
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 11629,
                "length": 3.3
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.25803683722294,
                            51.6148526981605
                        ],
                        [
                            -1.22435490208312,
                            51.6140866024406
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 13359,
                "length": 1.3
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.12972742224083,
                            51.587626761905
                        ],
                        [
                            -1.11110647051378,
                            51.5876670947644
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A415",
                "traffic": 17932,
                "length": 0.4
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.28543294417051,
                            51.6701488702853
                        ],
                        [
                            -1.28197758152293,
                            51.6728521889952
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A34",
                "traffic": 55022,
                "length": 11.8
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.31016478282563,
                            51.458680651855
                        ],
                        [
                            -1.29828665921033,
                            51.553637737088
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4130",
                "traffic": 9782,
                "length": 8.7
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.10356919925638,
                            51.5966013607872
                        ],
                        [
                            -0.989547947380133,
                            51.5756241007487
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4074",
                "traffic": 8140,
                "length": 14.7
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -0.998335099385856,
                            51.4843434675537
                        ],
                        [
                            -1.11110647051378,
                            51.5876670947644
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "road",
                "roadnumber": "A4074",
                "traffic": 18324,
                "length": 1.1
            },
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [
                            -1.11110647051378,
                            51.5876670947644
                        ],
                        [
                            -1.10356919925638,
                            51.5966013607872
                        ]
                    ]
                ]
            }
        }
    ]
}
    return data
