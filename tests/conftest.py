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
                "name": "Grim's Ditch; section 600yds (550m) long on East Ginge Down",
                "type": "monument"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.35711307254206,
                    51.5661547905162
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
                "type": "Point",
                "coordinates": [
                    -1.2892109818117,
                    51.6837622099323
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
                "type": "Point",
                "coordinates": [
                    -1.13467728496191,
                    51.6556706308269
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
                "type": "Point",
                "coordinates": [
                    -1.2806100994504,
                    51.6167284821114
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
                "type": "Point",
                "coordinates": [
                    -1.1207516332245,
                    51.613307190284
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
                "type": "Point",
                "coordinates": [
                    -1.30043835995313,
                    51.5952687707253
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
                "type": "Point",
                "coordinates": [
                    -1.24534907877791,
                    51.6636087954115
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
                "type": "Point",
                "coordinates": [
                    -1.18382921973757,
                    51.6672212045913
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
                "type": "Point",
                "coordinates": [
                    -1.30684035471683,
                    51.6090636612318
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
                "type": "Point",
                "coordinates": [
                    -1.28152109832397,
                    51.6715411557998
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
                "type": "Point",
                "coordinates": [
                    -1.29801515902622,
                    51.6695683429367
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
                "type": "Point",
                "coordinates": [
                    -1.20829873037113,
                    51.694362780306
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
                "type": "Point",
                "coordinates": [
                    -1.26918111978116,
                    51.6943165705608
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
                "type": "Point",
                "coordinates": [
                    -1.17877314103447,
                    51.5973312387089
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
                "type": "Point",
                "coordinates": [
                    -1.13839914671395,
                    51.5641327865591
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
                "type": "Point",
                "coordinates": [
                    -1.19278305240772,
                    51.6580758499934
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
                "type": "Point",
                "coordinates": [
                    -1.30409210625312,
                    51.5857325425876
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
                "type": "Point",
                "coordinates": [
                    -1.3604697222294,
                    51.5949546630729
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
                "type": "Point",
                "coordinates": [
                    -1.30688917633811,
                    51.6437933042357
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
                "type": "Point",
                "coordinates": [
                    -1.33672034162554,
                    51.669384089834
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
                "type": "Point",
                "coordinates": [
                    -1.23387514581252,
                    51.568436279247
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
                "type": "Point",
                "coordinates": [
                    -1.15692787879399,
                    51.6445930974072
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
                "type": "Point",
                "coordinates": [
                    -1.28324879440082,
                    51.670189515777
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
                "type": "Point",
                "coordinates": [
                    -1.29797963216915,
                    51.5627678276496
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
                "type": "Point",
                "coordinates": [
                    -1.15329139732202,
                    51.5312868903388
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
                "type": "Point",
                "coordinates": [
                    -1.29704629058976,
                    51.5718436707401
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
                "type": "Point",
                "coordinates": [
                    -1.27626539149497,
                    51.6814758207361
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
                "type": "Point",
                "coordinates": [
                    -1.22609756716941,
                    51.610550961041
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
                "type": "Point",
                "coordinates": [
                    -1.24119571523403,
                    51.6144708576188
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
                "type": "Point",
                "coordinates": [
                    -1.12041694600567,
                    51.5876472976218
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
                "type": "Point",
                "coordinates": [
                    -1.28370531434468,
                    51.671500542698
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
                "type": "Point",
                "coordinates": [
                    -1.30423213044639,
                    51.5061595600564
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
                "type": "Point",
                "coordinates": [
                    -1.04654527847476,
                    51.5861265187696
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
                "type": "Point",
                "coordinates": [
                    -1.05465715207522,
                    51.5360187312564
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
                "type": "Point",
                "coordinates": [
                    -1.10733820652602,
                    51.5921342917369
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": ""
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.26810891166814,
                    51.6328804155471
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "National\r\nPower Plc"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.24367383461684,
                    51.6754029312736
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": ""
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.27581375970588,
                    51.6734608951868
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC Limited"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.31024382134045,
                    51.6350287103914
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "Thames Water"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.17560451083803,
                    51.6449123308464
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "M L Parker"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.24796196859382,
                    51.6859645202037
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC\r\nLimited"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.31547514340399,
                    51.6337512701145
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "Oxfordshire Highways"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.34630491382614,
                    51.5983703806159
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "H S Raynor"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.29176826174873,
                    51.6262153240203
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC Limited"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.26584440907651,
                    51.6352844903224
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC Limited"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.25278048046993,
                    51.6302398847646
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC Limited"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.24942904559911,
                    51.6377549146346
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "Oxfordshire County Council"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.33775987095526,
                    51.677427069764
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "Tuckwells"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.23307182072792,
                    51.6820128263116
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "J Curtis and Sons"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.28698949651945,
                    51.6571554353294
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "J Curtis and Sons"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.29202780839381,
                    51.6505271122317
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "Thames Water"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.26584145907056,
                    51.6491343354668
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC Limited"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.16174439429281,
                    51.657735268529
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "ARC"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.16241131301098,
                    51.6540996801051
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "landfill",
                "name": "Mr Pratt"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.16627422349311,
                    51.6503690664972
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "ABINGDON (OXON STW"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.29023400482192,
                    51.6525458905304
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "BENSON, HENLEY ROA"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.10591156441916,
                    51.6096569683235
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "CHOLSEY, CHOLSEY,"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.14847942810127,
                    51.5805710109343
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "CULHAM, CULHAM, CL"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.22224255617706,
                    51.6557120182403
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "DIDCOT, FOXHALL RO"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.25117697460096,
                    51.6192149712736
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "DORCHESTER STW (OX"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.16329570438292,
                    51.6382232186528
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "DRAYTON, DRAYTON,"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.30348721780704,
                    51.6366205266501
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "type": "urbanwastewater",
                "name": "ABINGDON STW"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -1.29023400482192,
                    51.6525458905304
                ]
            }
        }
    ]
}
    return data
