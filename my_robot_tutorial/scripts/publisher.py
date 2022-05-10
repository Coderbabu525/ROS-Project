import rospy
from std_msgs.msg import String

def hello_world_pub():
    rospy.init_node("hello_world_pub_node")		#initialize the ros node
    pub = rospy.Publisher("hello_world", String, queue_size=10)		#publishing the topic name
    i = 0
    rate = rospy.Rate(5)		#5 msgs are sending in a second
    while not rospy.is_shutdown():		#for looping upto any interrupt
        pub.publish("Hello World" + str(i))		#publishing the value of RPM
        i += 1
        rate.sleep()


if __name__ == '__main__':
    try:
        hello_world_pub()		#invoking publisher method
    except rospy.ROSInterruptException:
        pass
