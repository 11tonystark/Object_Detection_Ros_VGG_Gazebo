#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

def callback(data):
    br = CvBridge()
    rospy.loginfo('receiving image')
    try:
      data.encoding = 'rgb8'
      cv_image = br.imgmsg_to_cv2(data, "rgb8")
    except CvBridgeError as e:
      print(e)
    #cv2.imshow("camera",cv_image)
    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_green = np.array([40,70,70])
    upper_green = np.array([80,230,230])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(cv_image,cv_image, mask= mask)

    cv2.imshow('cv_image',cv_image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    a=np.sum(res)
    print(a)
    if a>230000:
    	print(a)
        print('keep moving ')

    
 
    ##cv2.waitKey(1)


def listener():
    rospy.init_node('listener', anonymous=True,disable_signals=True)

    rospy.Subscriber('/r200/camera/color/image_raw', Image, callback)

    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    listener()
