"""
Receives a geojson bundle for

- substations
- motorway junctions
- rail stations

Calculate weighted index of distance to substations

"""
import geopy.distance
import geopandas as gpd

def parse_geojson(geojson, feature_type):

    data = gpd.GeoDataFrame.from_features(geojson)
    data = data[data['type'] == feature_type]

    list_of_points = [x.coords[:] for x in data['geometry']]

    return list_of_points

def compute_inverse_distance(centroid, substation, buffer_km):

    dist = geopy.distance.vincenty(centroid, substation).km
    inverse_distance = buffer_km - dist

    return inverse_distance

def calculate_substation_index(centroid, substation_geojson, buffer_km):

    list_of_substation_locations = parse_geojson(substation_geojson, 'substation')
    
    distances = []
    for substation in list_of_substation_locations:
        distance = compute_inverse_distance(centroid, substation, buffer_km)
        distances.append(distance)

    index_value = sum(distances) / len(distances)
    
    return index_value

def calculate_road_index(geojson):

    frame = gpd.GeoDataFrame.from_features(geojson)
    roads = frame[frame['type']=='road']
    roads['aggregate_congestion'] = None

    for index, road in roads.iterrows():

        if road['roadnumber'][0] == 'A':
            lanes = 2
            maxcap = 1380
        elif road['roadnumber'][0] == 'B':
            lanes = 2
            maxcap = 1150
        elif road['roadnumber'][0] == 'M':
            lanes = 2
            maxcap = 2330

        # 'Flow in the busiest hour is assumed to be 10.5% of the daily flow

        congestion_level = road["traffic"] * 0.105 / lanes / maxcap
        roads.loc[index, 'aggregate_congestion'] = congestion_level * road["length"]

    Totalcongestion = roads['aggregate_congestion'].sum()
    Totallength = roads['length'].sum()

    Meancongestion = Totalcongestion / Totallength

    return Meancongestion
