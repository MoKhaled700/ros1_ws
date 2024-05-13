#!/usr/bin/env python3
from Lab2.srv import AddTwoInts,AddTwoIntsResponse
import rospy
def handle_add_two_ints(req):
    return AddTwoIntsResponse(req.a + req.b)
def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()
if __name__ == "__main__":
    add_two_ints_server()