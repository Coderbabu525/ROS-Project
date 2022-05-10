#!/usr/bin/python3

import rospy
from mini_formative_project.srv import TurnCamera, TurnCameraResponse

import os
import cv2
from cv_bridge import CvBridge


class TurnCameraClass:
    def __init__(self):
        self.available_angles = [-30, -15, 0, 15, 30]       #images available of these angles
        self.ros_service = rospy.Service("turn_camera", TurnCamera, self.send_image) #creation of ros service

    def read_in_image_by_filename(self, file_name):
        dir_name = os.path.dirname(__file__)    #getting current directory
        file_location = dir_name + "/Images/" + file_name      #full path to image
        image = cv2.imread(file_location)       #reading the image
        return image
    def get_image(self, angle):
        closest_angle = min(self.available_angles, key=lambda x:abs(x-angle)) #calculating closest angle for which image is available
        return self.read_in_image_by_filename(str(closest_angle) + ".png")     #sending the image filename

    def send_image(self, req):
        image = self.get_image(req.turn_degrees)        #getting the input degree
        image_msg = CvBridge().cv2_to_imgmsg(image)     #converting image as a msg
        return TurnCameraResponse(image_msg)            #sending that image msg as an array

if __name__ == '__main__':
    try:
        rospy.init_node("turn_camera_service_node")     # initialization
        TurnCameraClass()                               #calling the class
        print("Turn Camera Service is running")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
