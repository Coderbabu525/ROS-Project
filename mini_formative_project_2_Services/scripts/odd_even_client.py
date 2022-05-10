#!/usr/bin/python3

import rospy
from mini_formative_project_2_Services.srv import OddEvenCheck, OddEvenCheckResponse	#importing the services


if __name__ == '__main__':
    rospy.init_node("odd_even_client_node")		#node name initilization
    srv_proxy = rospy.ServiceProxy("odd_even_check", OddEvenCheck)		# to interact with service

    user_input = input("\nEnter a whole number: ")		# to get user input number to be checked
    resp_obj = srv_proxy(int(user_input))		#to send the service request
    answer = resp_obj.answer		#answer coming from sevice
    print(answer)
