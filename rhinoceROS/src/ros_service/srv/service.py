#!/usr/bin/env python

import rospy
from ros_service.srv import *
from math import *

def getPathLength(lat1,lng1,lat2,lng2):
    '''calculates the distance between two lat, long coordinate pairs'''
    R = 6371000 # radius of earth in m
    lat1rads = radians(lat1)
    lat2rads = radians(lat2)
    deltaLat = radians((lat2-lat1))
    deltaLng = radians((lng2-lng1))
    a = sin(deltaLat/2) * sin(deltaLat/2) + cos(lat1rads) * cos(lat2rads) * sin(deltaLng/2) * sin(deltaLng/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c
    return d

def getDestinationLatLong(lat,lng,azimuth,distance):
    '''returns the lat an long of destination point
    given the start lat, long, aziuth, and distance'''
    R = 6378.1 #Radius of the Earth in km
    brng = radians(azimuth) #Bearing is degrees converted to radians.
    d = distance/1000 #Distance m converted to km
    lat1 = radians(lat) #Current dd lat point converted to radians
    lon1 = radians(lng) #Current dd long point converted to radians
    lat2 = asin(sin(lat1) * cos(d/R) + cos(lat1)* sin(d/R)* cos(brng))
    lon2 = lon1 + atan2(sin(brng) * sin(d/R)* cos(lat1), cos(d/R)- sin(lat1)* sin(lat2))
    #convert back to degrees
    lat2 = degrees(lat2)
    lon2 = degrees(lon2)
    return[lat2, lon2]

def calculateBearing(lat1,lng1,lat2,lng2):
    '''calculates the azimuth in degrees from start point to end point'''
    startLat = radians(lat1)
    startLong = radians(lng1)
    endLat = radians(lat2)
    endLong = radians(lng2)
    dLong = endLong - startLong
    dPhi = log(tan(endLat/2.0+pi/4.0)/tan(startLat/2.0+pi/4.0))
    if abs(dLong) > pi:
         if dLong > 0.0:
             dLong = -(2.0 * pi - dLong)
         else:
             dLong = (2.0 * pi + dLong)
    bearing = (degrees(atan2(dLong, dPhi)) + 360.0) % 360.0
    return bearing

def waypoint_generator(interval,azimuth,lat1,lng1,lat2,lng2):
    global coords
    '''returns every coordinate pair inbetween two coordinate
    pairs given the desired interval'''

    d = getPathLength(lat1,lng1,lat2,lng2)
    remainder, dist = modf((d / interval))
    counter = float(interval)
    coords = []
    coords.append([lat1,lng1])
    for distance in range(0,int(dist)):
        coord = getDestinationLatLong(lat1,lng1,azimuth,counter)
        counter = counter + float(interval)
        coords.append(coord)
    coords.append([lat2,lng2])
    return coords


RoverX = 0
RoverY = 0
# point interval in meters
interval = 1.0
# direction of line in degrees
# start point
lat1 = 38.419354
lng1 = -110.781900
# end point
lat2 = 38.419349
lng2 = -110.780511


coords = []
lat_list =[]
lon_list = []

def callback_path(req):
    global coords,lat_list,lon_list
    azimuth = calculateBearing(lat1, lng1, lat2, lng2)
    coords = waypoint_generator(interval, azimuth, lat1, lng1, lat2, lng2)
    for i in coords:
        lat_list.append(i[0])
        lon_list.append(i[1])
    return PathResponse(lat_list,lon_list)


def gps_server():
    rospy.init_node('GPS_SERVER', anonymous = True ,disable_signals=True)

    s = rospy.Service('gps_service', Path, callback_path)

    while not rospy.is_shutdown():
        rospy.sleep(0.01)

if __name__ == "__main__":
    gps_server()

