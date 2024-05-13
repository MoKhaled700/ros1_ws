#! /usr/bin/env python3
import rospy
import actionlib
from Lab2.msg import CounterAction, CounterGoal
def feedback_cb(msg):
    print('Feedback received: ' + str(msg))
def call_server():
    client = actionlib.SimpleActionClient('Counter', CounterAction)
    client.wait_for_server()
    goal = CounterGoal()
    goal.Limit = 20
    client.send_goal(goal,feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
    print('The result is: ' + str(result))
if __name__ == '__main__':
    rospy.init_node('action_client')
    call_server()
