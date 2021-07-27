#!/usr/bin/env python

import rospy
from hello_world.msg import Msg_1

def publisher():
    #Initialize node (NodeName, anonymous)
    rospy.init_node("helloworld_pub")

    #Initialize topic (TopicName, MessageType)
    pub = rospy.Publisher("hw_topic",Msg_1, queue_size = 10)

    #Set publish cycle
    rate = rospy.Rate(1)
    msg = Msg_1()
    msg.x = 0
    msg.y = 0

    count = 0
    while not rospy.is_shutdown():

        msg_param = rospy.get_param("~message")
        
        #create publish message
        input_str = raw_input('Enter:')

        if input_str == "D":
            msg.x += msg_param
            msg.y = msg.y
        elif input_str == "A":
            msg.x -= msg_param
            msg.y = msg.y
        elif input_str == "W":
            msg.x = msg.x
            msg.y += msg_param
        elif input_str == "X":
            msg.x = msg.x
            msg.y -= msg_param
        elif input_str == "S":
            msg.x = 0
            msg.y = 0
        else:
            pass

        #send message
        pub.publish(msg)

        count+=1
        rospy.loginfo("count: {} -> message: x :{} y: {}".format(count,str(msg.x),str(msg.y)))
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
