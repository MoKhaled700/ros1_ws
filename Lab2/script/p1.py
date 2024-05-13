#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from Lab2.srv import Age, AgeResponse
from Lab2.msg import CounterAction, CounterFeedback, CounterResult
import actionlib

i = 0  # Initialize 'i' outside the pub function

#Action Srever
global Action_Server
def Action():
    global Action_Server
    Action_Server = actionlib.SimpleActionServer("Counter", CounterAction, callback_action, auto_start=False)
    Action_Server.start()

def callback_action(goal):
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



# Callback function for the Age service
def callback_serv(request):
    # Create and return an AgeResponse
    response = AgeResponse('Happy '+str(request)+'th Birthday!!')
    Action()
    return response

def pub():
    global i  # Use the global 'i' variable

    pub = rospy.Publisher('month', String, queue_size=10)
    rospy.init_node('pub', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        msg = String()
        i = i + 1
        msg.data = 'Month ' + str(i)
        pub.publish(msg)
        print(msg.data)
        rate.sleep()
        if i==12:
            break

if __name__ == '__main__':
    try:
        rospy.Service('Age', Age, callback_serv)
        pub()
        # Define the Age service outside the pub function
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
