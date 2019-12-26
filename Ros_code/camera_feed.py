#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def callback(data):
    br = CvBridge()
    rospy.loginfo('receiving image')
    try:
      data.encoding = 'rgb8'
      cv_image = br.imgmsg_to_cv2(data, "rgb8")
    except CvBridgeError as e:
      print(e)
    cv2.imshow("camera",cv_image)
    cv2.waitKey(1)


def listener():
    rospy.init_node('listener', anonymous=True,disable_signals=True)

    rospy.Subscriber('/r200/camera/color/image_raw', Image, callback)

    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    listener()
