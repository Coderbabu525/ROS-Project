import rospy;


if __name__ == "__main__":
    rospy.init_node('my_first_python_node')		#initialization

    rospy.loginfo("This node has started running")		#to make confirm that the node is running

    rate = rospy.Rate(10)		#10 msgs are sending in a second

    while not rospy.is_shutdown():
        rospy.loginfo("Hello World!")		#printing the 'hello world' message
        rate.sleep()
