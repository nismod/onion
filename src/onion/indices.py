"""
Receives a geojson bundle for

- substations
- motorway junctions
- rail stations

Calculate weighted index of distance to substations

"""
import geopy.distance
import geopandas as gpd

def parse_geojson(geojson):

    data = gpd.GeoDataFrame.from_features(geojson)

    list_of_points = [x.coords[:] for x in data['geometry']]

    return list_of_points

def compute_inverse_distance(centroid, substation, buffer_km):

    dist = geopy.distance.vincenty(centroid, substation).km
    inverse_distance = buffer_km - dist

    return inverse_distance

def calculate_substation_index(centroid, substation_geojson, buffer_km):

    list_of_substation_locations = parse_geojson(substation_geojson)
    
    distances = []
    for substation in list_of_substation_locations:
        distance = compute_inverse_distance(centroid, substation, buffer_km)
        distances.append(distance)

    index_value = sum(distances) / len(distances)
    
    return index_value
