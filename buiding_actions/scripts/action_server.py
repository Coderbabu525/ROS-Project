#!/usr/bin/python3

import math
import rospy
import actionlib
from building_actions.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point

class Navigate2DClass:
    def __init__(self):     #for initializing the class
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action", Navigate2DAction, self.navigate_cb) #initilizing the server
        self.robot_point_sub = rospy.Subscriber("robot/point", Point, self.update_robot_position)   #creating subscriber node
        self.robot_current_point = None     #initilization
        self.robot_goal_point = None        #initilization
        self.distance_threshold = 0.35      #initilization
        self.feedback_rate = rospy.Rate(1)  #initilization of feedback time
    def navigate_cb(self, goal):    #navigate callback
        navigate_start_time = rospy.get_time()      #getting current time
        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]  #setting the goal point

        while self.robot_current_point == None:
            print("Robot point not detected")
            rospy.sleep(5)

        print("Robot point detected")
        distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)		#retrieving distance to goal

        while distance_to_goal>self.distance_threshold:		#continously checking the distance to give feedback
            self.action_server.publish_feedback(Navigate2DFeedback(distance_to_point = distance_to_goal))
            self.feedback_rate.sleep()
            distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        navigate_end_time = rospy.get_time()		#ending time

        elapsed_time = navigate_end_time - navigate_start_time		#calculating elapsed time taken by the robot

        rospy.loginfo("Navigation succesful, Elapsed time: " + str(elapsed_time) + "secs")		# to see the output

        self.action_server.set_succeeded(Navigate2DResult(elapsed_time))		#set the succeed status


    def update_robot_position(self, point):     #for modifying robot position
        self.robot_current_point = [point.x, point.y, point.z]

if __name__ == '__main__':
    rospy.init_node("navigate_2D_action_server_node")       #initilizing node name
    server = Navigate2DClass()      #calling the class
    rospy.spin()        #for continious run
