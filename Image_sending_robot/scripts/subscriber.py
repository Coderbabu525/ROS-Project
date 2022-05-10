#!/usr/bin/python3

import rospy
from std_msgs.msg import String, Float64


def process_robot_data(rpm, publisher):
    wheel_radius = rospy.get_param("/wheel_radius")          #wheel diameter value is fixed
    speed = (rpm.data * 2 * wheel_radius * 3.1416) / 60.0   #receiving and using the RPM data
    publisher.publish(speed)
    #print("Robot speed is: " + str("{:.2f}".format(speed)) + "m/s")  #print calculated speed
def create_subscriber_node(pub):
    rospy.init_node("robot_data_sub_node")
    rospy.Subscriber("RPM", Float64, process_robot_data, (pub))  #subscribing to the RPM topic

def speed_pub():
    pub = rospy.Publisher("speed", Float64, queue_size=10)
    return pub

if __name__ == '__main__':
    #rospy.init_node("calc_speed_sub_node")
    pub = speed_pub()
    create_subscriber_node(pub)
    rospy.spin()
