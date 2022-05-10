import rospy
from std_msgs.msg import String, Float64

def robot_data_pub():
    rospy.init_node("robot_data_pub_node")    #initialize the ros node
    rpm = rospy.Publisher("RPM", String, queue_size = 10)  #publishing the topic name
    rate = rospy.Rate(5)		#5 msgs are sending in a second
    while not rospy.is_shutdown():
        rpm.publish(str(80))     #publishing the value of RPM
        rate.sleep()

if __name__ == '__main__':
    try:
        robot_data_pub()		#invoking publisher method
    except rospy.ROSInterruptException:
        pass


#Note: We're passing the rpm in string because we will print it from subscriber's end