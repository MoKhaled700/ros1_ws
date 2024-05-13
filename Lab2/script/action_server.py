#! /usr/bin/env python3
import rospy
import actionlib
from Lab2.msg import CounterAction, CounterFeedback, CounterResult 
global Action_Server
def Action():
    global Action_Server
    rospy.init_node("action_server")
    Action_Server = actionlib.SimpleActionServer("Counter", CounterAction, callback, auto_start=False)
    Action_Server.start()

def callback(goal):
    global Action_Server
    feedback = CounterFeedback()
    result = CounterResult()
    rate = rospy.Rate(1)
    Final_Number = 0
    for i in range(0, goal.Limit):
        feedback.current = i+1
        Action_Server.publish_feedback(feedback)
        Final_Number = Final_Number+1
        rate.sleep()
        result.Limit_Reached = Final_Number
        Action_Server.set_succeeded(result)
if __name__ == "__main__":
    Action()
    rospy.spin()
