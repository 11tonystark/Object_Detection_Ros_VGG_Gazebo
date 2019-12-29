#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from math import atan,pi,sin



threshold=0.5


ob1=Twist()


psd1L=Range()
psd1R=Range()
psd2L=Range()
psd2R=Range()

X1_slope = 0.00
slope_angle = 0.00
X2_o = 0.79
X2_T = 0.02
X1_o = 0.95
X1_T = 0.02

alpha = 45
L = 0.1326



def callback1(msg):        #X1
    global psd1L,X1_slope
    psd1L = msg.range
    psd1L = round(psd1L,2)
    X1_slope = psd1L - X1_o - X1_T + X2_o - X2_T
    #print(abs(psd1L-0.95))

def callback2(msg):
    global psd1R
    psd1R= msg.range
    psd1R = round(psd1R, 2)

def callback3(msg):        #X2
    global psd1L,psd2L,slope_angle
    psd2L= msg.range
    psd2L = round(psd2L, 2)

    slope_angle = 90 - alpha - ((180 / pi) * atan((psd1L - psd2L) / L))
    #print(abs(psd2L - 0.79))
    if ( ( (psd1L-X1_o>X1_T) and (psd2L-X2_o>X2_T) ) and  ( abs(psd1L-X1_o)-X1_T < abs(psd2L-X2_o) +X2_T )   ):
        ditch_depth= ( X2_o-psd2L) *sin(pi/2)
        print("DITCH APPROACHING","DITCH DEPTH=",ditch_depth)



def callback4(msg):
    global psd2R
    psd2R= msg.range
    psd2R = round(psd2R, 2)

def calculate():

    global psd1L,psd1R,psd2L,psd2R,X_slope

    X1 = psd1L
    X2 = psd2L



    #flat floor

    if (   ( (X1<= X1_o+X1_T) and (X1>=X1_o-X1_T) )  and  ( (X2<= X2_o+X2_T) and (X2>=X2_o-X2_T) ) ):
        print("FLAT")

    elif ( (((X1 > X1_o+X1_T) or (X1 < X1_o -X1_T)) and ((X2 > X2_o+X2_T) or (X2 < X2_o -X2_T))) and (X1_slope < X2)  ):

        print("UPWARD SLOPE APPROACHING","SLOPE ANGLE=",slope_angle)
              

    #else:
     #   print("NON-F")



def listener():


    rospy.Subscriber("psd1l_topic", Range, callback1)
    rospy.Subscriber("psd1r_topic", Range, callback2)
    rospy.Subscriber("psd2l_topic", Range, callback3)
    rospy.Subscriber("psd2r_topic", Range, callback4)

    while not rospy.is_shutdown():


        calculate()
        rospy.sleep(0.01)



if __name__ == '__main__':
    try:

        rospy.init_node('Communication', anonymous=True,disable_signals=True)
        rate = rospy.Rate(50) 

        listener()

    except rospy.ROSInterruptException:
        pass
