#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import NavSatFix
from math import *
from pyproj import Geod


def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def haversine(lat1, lon1, lat2, lon2):
    # distance between latitudes
    # and longitudes
    global dist
    degree,rev_degree,dist = wgs84_geod.inv(lon1, lat1, lon2, lat2)


def bearing(lat1, lon1, lat2, lon2):
    global degree
    degree,rev_degree,dist = wgs84_geod.inv(lon1, lat1, lon2, lat2)
    if degree < 0:
        degree += 360

pitch = 0.0
roll = 0.0
yaw = 0.0

threshold = 0.45
b_threshold = 0.2

ob1 = Twist()

f = open("lat_only.txt", "r")
g = open("lon_only.txt", "r")


def forward():
    # print("FORWARD")
    ob1.linear.x = 0.5
    ob1.linear.y = 0
    ob1.linear.z = 0

    ob1.angular.x = 0
    ob1.angular.y = 0
    ob1.angular.z = 0
    pub.publish(ob1)


def backward():
    # print("BACKWARD")
    ob1.linear.x = -0.3
    ob1.linear.y = 0
    ob1.linear.z = 0

    ob1.angular.x = 0
    ob1.angular.y = 0
    ob1.angular.z = 0

    pub.publish(ob1)


def right():
    # print("RIGHT")
    ob1.linear.x = 0
    ob1.linear.y = 0
    ob1.linear.z = 0

    ob1.angular.x = 0
    ob1.angular.y = 0
    ob1.angular.z = 2.5
    pub.publish(ob1)


def left():
    # print("LEFT")
    ob1.linear.x = 0
    ob1.linear.y = 0
    ob1.linear.z = 0

    ob1.angular.x = 0
    ob1.angular.y = 0
    ob1.angular.z = -2.5
    pub.publish(ob1)


def brutestop():
    # print("BRUTESTOP")
    ob1 = Twist()
    pub.publish(ob1)


heading = 0
degree = 0
dist = 10
lat1=0
lon1=0

def callback_imu(msg):
    global heading

    orientation_list = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

    heading = arduino_map(yaw, 0, -3, 0, 180)

    if heading < 0:
        heading += 360


def callback_gps(msg):
    global lat1, lon1

    lat1 = msg.latitude
    lon1 = msg.longitude


def waypoint_replay(lat2,lon2):
    global lat1, lon1

    haversine(lat1, lon1, lat2, lon2)
    bearing(lat1, lon1, lat2, lon2)


def displaydata(t, dist):
    if t < 10 and t > -10:
        print("STRAIGHT", "DISTANCE=", dist)
        forward()

    elif t <= -180:
        angle = 360 + t
        print("ANTICLOCKWISE", angle, "DISTANCE=", dist)
        left()


    elif t < 0 and t > -180:
        angle = -t
        print("CLOCKWISE", angle, "DISTANCE=", dist)
        right()


    elif t >= 180:
        angle = 360 - t
        print("CLOCKWISE", angle, "DISTANCE=", dist)
        right()

    elif t > 0 and t < 180:
        angle = t
        print("ANTICLOCKWISE", angle, "DISTANCE=", dist)
        left()


def listener():
    global dist
    rospy.Subscriber("imu_data", Imu, callback_imu)
    rospy.Subscriber("gps_topic", NavSatFix, callback_gps)

    while not rospy.is_shutdown():


        rospy.sleep(0.01)

        f1 = f.readlines()
        g1 = g.readlines()

        for latitude, longitude in zip(f1, g1):
            lat2 = float(latitude)
            lon2 = float(longitude)

            while (dist>0.3):

                waypoint_replay(lat2,lon2)
                t = heading - degree
                displaydata(t, dist)

            print("WAYPOINT REACHED")
            dist =10
            continue

        print("GOAL REACHED")
        brutestop()
        break

if __name__ == '__main__':
    try:
        global ob1
        pub = rospy.Publisher('champ', Twist, queue_size=10)
        rospy.init_node('Communication', anonymous=True)
        rate = rospy.Rate(50)  # 1hz


        listener()

    except rospy.ROSInterruptException:
        pass

