from argparse import ArgumentParser

import gpxpy
import gpxpy.gpx
import os

parser = ArgumentParser()

parser.add_argument("-d", "--directory", dest="directory",
                    required=True, help="path to directory containing gpx files")

parser.add_argument("-o", "--output", dest="output",
                    required=True, help="path to output")


args = parser.parse_args()

# Example for how you could print all points
# for track in gpx.tracks:
#     for segment in track.segments:
#         for point in segment.points:
#             print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

# for waypoint in gpx.waypoints:
#     print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))

# for route in gpx.routes:
#     print('Route:')
#     for point in route.points:
#         print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))



# There are many more utility methods and functions:
# You can manipulate/add/remove tracks, segments, points, waypoints and routes and
# get the GPX XML file from the resulting object:

directoy = args.directory
output = args.output

merged = gpxpy.gpx.GPX()
for root, _, files in os.walk(directoy):
    for file in files:
        print(file)
        if file.endswith(".gpx"):
            gpx_file = open("/".join([root,file]), 'r')
            gpx = gpxpy.parse(gpx_file)
            for track in gpx.tracks:
                track.name = file
                merged.tracks.append(track)
            for route in gpx.routes:
                route.name = file
                merged.routes.append(route)
            for wp in gpx.waypoints:
                merged.waypoints.append(wp)


with open(output, "w") as f:
    f.write(merged.to_xml())
