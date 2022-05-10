import rospy
from std_msgs.msg import String, Float64

def process_robot_data(data):
    diameter = 20.7          #wheel diameter value is fixed
    speed = (float(data.data) * diameter * 3.1416) / 60.0   #receiving and using the RPM data
    print("Robot speed is: " + str("{:.2f}".format(speed)) + "m/s")  #print calculated speed
def create_subscriber_node():
    rospy.init_node("robot_data_sub_node")
    rospy.Subscriber("RPM", String, process_robot_data)  #subscribing to the RPM topic


if __name__ == '__main__':
    create_subscriber_node()
    rospy.spin()
