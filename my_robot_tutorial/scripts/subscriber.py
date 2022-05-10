import rospy
from std_msgs.msg import String

def process_hello_world_msg(data):
    print("Message Received " + str(data))		#printing the receipt message
def create_subscriber():
    rospy.init_node("hello_world_sub_node")		#initialization
    rospy.Subscriber("hello_world", String, process_hello_world_msg)		#subscribing to the topic


if __name__ == '__main__':
    create_subscriber()		#invoking subscriber
    rospy.spin()
