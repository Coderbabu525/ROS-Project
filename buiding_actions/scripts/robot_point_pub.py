#!/usr/bin/python3

import rospy

from geometry_msgs.msg import Point

def robot_point_pub(user_coords):
    pub = rospy.Publisher("robot/point", Point, queue_size=10)  #setting the publisher
    print("Publishing")

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(Point(x=user_coords[0], y = user_coords[1], z = user_coords[2]))    #publishing the current point
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node("robot_point_pub_node") #initializing the publisher node

        user_x = input("What is your current x-coordinates?: ")
        user_y = input("What is your current y-coordinates?: ")
        user_z = input("What is your current z-coordinates?: ")

        user_coords = [float(user_x), float(user_y), float(user_z)]		#packing up the 3 values in a single coordinate variable

        robot_point_pub(user_coords)		#invoking the method and sending the coordinate


    except rospy.ROSinterruptException:
        print("Exception Occured")
