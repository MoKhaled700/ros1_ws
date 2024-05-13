#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from Lab2.srv import AddTwoInts,AddTwoIntsResponse
import math
def turtle():
    rospy.init_node('turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
    s = rospy.Service('add_two_ints', AddTwoInts,handle_add_two_ints)
    rate = rospy.Rate(10) # 10hz
    vel = Twist()
    while not rospy.is_shutdown():
         t = 0
         rate = rospy.Rate(10)  # 10hz
         while not rospy.is_shutdown() and t <= 2* math.pi:
            vel = Twist()
            vel.linear.x = 0.1 * math.sin(t)**3
            vel.linear.y = -0.1 * math.cos(t) + 2 * math.cos(2*t) + 2 * math.cos(3*t) + 0.5 * math.cos(4*t)
            vel.linear.z = 0
            vel.angular.x = 0
            vel.angular.y = 0
            vel.angular.z = 0
            pub.publish(vel)
            t += 0.05
            rate.sleep()

def pose_callback(pose):
    print(pose.x, pose.y,pose.theta)
def handle_add_two_ints(req):
 return AddTwoIntsResponse(req.a + req.b)
if __name__ == '__main__':
    try:
       turtle()
    except rospy.ROSInterruptException:
       pass