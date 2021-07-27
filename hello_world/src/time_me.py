#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("measuring_time_pub")
    pub = rospy.Publisher("hello_time",String,queue_size=10)
    msg = String()
    rate = rospy.Rate(1)

    s_time = rospy.get_time()
    while not rospy.is_shutdown():
        msg_text = 'hello'
        msg.data = msg_text
        pub.publish(msg)
        rate.sleep()

    result = rospy.get_time() - s_time
    print("time: {}".format(result))


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
