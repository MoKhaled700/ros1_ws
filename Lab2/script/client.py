#!/usr/bin/env python3
import sys
import rospy
from Lab2.srv import AddTwoInts
def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
    resp1 = add_two_ints(x, y)
    return resp1.sum
if __name__ == "__main__":
    rospy.init_node('client_node')
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
