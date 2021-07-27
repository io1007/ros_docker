#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import String

def publisher():
    #Initialize node (NodeName, anonymous)
    rospy.init_node("helloworld_pub")

    #Initialize topic (TopicName, MessageType)
    pub = rospy.Publisher("hw_topic",String, queue_size = 10)

    #Set publish cycle
    rate = rospy.Rate(1)

    count = 0
    while not rospy.is_shutdown():
        msg_text = random.uniform(-100.00,100.00)
        msg_text = str(msg_text)
        
        #create publish message
        msg = String()
        msg.data = msg_text

        #send message
        pub.publish(msg)

        count+=1
        rospy.loginfo("count: {} -> message: {}".format(count,msg_text))
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
