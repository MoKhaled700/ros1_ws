#!/usr/bin/env python3
import sys
import rospy
from std_msgs.msg import String
from Lab2.srv import Age, AgeResponse
import actionlib
from Lab2.msg import CounterAction, CounterGoal

#Action Client 
def feedback_cb(msg):
    print('Cakes Baked cake_baked: ' + str(msg))
def call_serverAction():
    client = actionlib.SimpleActionClient('Counter', CounterAction)
    client.wait_for_server()
    goal = CounterGoal()
    goal.Limit = 3
    client.send_goal(goal,feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
    print('result: Cakes Baked Enjoy!!' )



def callback(data):
    print ("it is " + data.data)
    if data.data == 'Month 12':
        x = int(sys.argv[1])
        res=client(x)
        print(res)
        call_serverAction()
        
        

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('month', String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def client(x):
    rospy.wait_for_service('Age')
    while not rospy.is_shutdown():
        age_client= rospy.ServiceProxy('Age', Age)
        res1=age_client(x)
        return res1.msg
        

if __name__ == '__main__':  
    listener()


