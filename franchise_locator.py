#This Python script determines which predefined region contains a given point using the shapely library.
from shapely.geometry import Polygon, Point
import json

with open("regions.json") as f:
    data = json.load(f)

cities = data["cities"]
regions = data["regions"]
region_num = 1

request_point = Point(26.1962, -13.3959)
# request_point = Point(48.9839, -104.574)  # Another example point

for region in regions:
    region_coordinates = list()
    for city in region:
        region_coordinates.append((cities[city][0], cities[city][1]))

    region_polygon = Polygon(region_coordinates)

    if region_polygon.contains(request_point):
        print(region_num)
        break

    region_num += 1
