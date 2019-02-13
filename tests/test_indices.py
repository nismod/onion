from onion.indices import compute_inverse_distance, parse_geojson, calculate_substation_index

def test_compute_substation_distance():

    centroid = (0, 0)
    substation = (10, 10)
    buffer_km = 0
    actual = compute_inverse_distance(centroid, substation, buffer_km)
    expected = -1565.1090992067398

    assert actual == expected

def test_parse_geojson(geojson):
    actual = parse_geojson(geojson)
    expected = [[(-1.16028744986759, 51.5351050684567)],
                [(-1.22835338989177, 51.6611686319984)],
                [(-1.25934538640586, 51.6255544962863)]]
    assert actual == expected

def test_calculate_substation_index(geojson):

    centroid = (-0.376931, 52.25207)
    buffer_km = 100

    actual = calculate_substation_index(centroid, geojson, buffer_km)
    expected = -17.517934296490335
    assert actual == expected
