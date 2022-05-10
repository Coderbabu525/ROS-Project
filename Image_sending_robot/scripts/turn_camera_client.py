#!/usr/bin/python3

import rospy
from Image_sending_robot.srv import TurnCamera, TurnCameraResponse

import os
import cv2
from cv_bridge import CvBridge

def configure_request(angle):
    rospy.wait_for_service("turn_camera")       #wait untill turn camera service becomes available
    try:
        service_proxy = rospy.ServiceProxy("turn_camera", TurnCamera)   # service proxy to call particular service
        resp_msg = service_proxy(angle)
        image_msg = resp_msg.image      #image msg provided from service
        image = CvBridge().imgmsg_to_cv2(image_msg, desired_encoding="passthrough")     #converting image msg to original image
        cv2.imshow("Turn Camera Image", image)      #show the image
        cv2.waitKey(0)      #shows image until any key is pressed
        cv2.destroyAllWindows()     #for closing the window in case
    except rospy.ServiceException as e:
        print("Service Request Failed.\n")      #showing any error
        print(e)        #printing the exception we got

if __name__ == '__main__':
    try:
        rospy.init_node("turn_camera_client_node")      #initialization
        user_input = input("\nEnter an anglein degree to move the robot camera. ")      #user input angle

        while user_input != 'q':        #for continious input
            try:
                configure_request(float(user_input))        #process request
                user_input = input("\nEnter an anglein degree to move the robot camera. ")
            except:
                print("Error trying to process request")

    except rospy.ROSInterruptException:
        pass
