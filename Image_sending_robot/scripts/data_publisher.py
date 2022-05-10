#!/usr/bin/python3

import rospy
from std_msgs.msg import String, Float64

def robot_data_pub():
    rospy.init_node("robot_data_pub_node")    #initialize the ros node
    rpm = rospy.Publisher("RPM", Float64, queue_size = 10)  #publishing the topic name
    #wheel_diameter = rospy.Publisher("wheel_diameter", String, queue_size = 10)
    rate = rospy.Rate(5)
    i = 0
    while not rospy.is_shutdown():
        rpm.publish(80)     #publishing the value of RPM
        #wheel_diameter.publish(str(20.7))
        i += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        robot_data_pub()
    except rospy.ROSInterruptException:
        pass
