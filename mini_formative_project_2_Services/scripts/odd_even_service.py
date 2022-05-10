#!/usr/bin/python3

import rospy
from mini_formative_project_2_Services.srv import OddEvenCheck, OddEvenCheckResponse		#importing services

def check_number(req):				#callback function to check odd even
    if(req.number % 2) ==0:
        check = "even"
    else:
        check = "odd"

    return OddEvenCheckResponse(check)

if __name__ == '__main__':
    try:
        rospy.init_node("odd_even_service_node")		# node name initilization
        rospy.Service("odd_even_check", OddEvenCheck, check_number)		# creating service
        rospy.spin()		#to keep running
    except rospy.ROSInterruptException:
        pass
