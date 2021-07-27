#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from datetime import datetime
import pytz


def callback(msg):
    dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    if msg.data == "date":
        result = dt_now.strftime("%Y:%m:%d")
    elif msg.data == "time":
        result = dt_now.strftime("%H:%M:%S")
    else:
        result = "No message is returnble"

    rospy.loginfo("I heard msg: {} --> {}".format(msg.data,result))

def subscriber():
    #Initialize & Setup Node (NodeName)
    rospy.init_node("helloworld_sub")

    #Set listen topic (TopicName, MessageType)
    rospy.Subscriber("hw_topic", String, callback)

    #start ROS node
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except Exception:
        print('Exception raised..')
