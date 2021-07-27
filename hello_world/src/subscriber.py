#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard message: {}".format(msg.data))


def subscriber():
    # Initialize & Setup Node (NodeName)
    rospy.init_node("helloworld_sub")

    # Set listen topic (TopicName, MessageType)
    rospy.Subscriber("hw_topic", String, callback)

    # start ROS node
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except Exception:
        print('Exception raised..')
