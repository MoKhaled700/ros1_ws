#!/usr/bin/env python3
import rospy
import numpy as np
import random
from turtlesim.msg import Pose

SD = [0.1, 0.1, 0.1] # Standard Deviation Inputs
def callback(poseData):
    # Extract the x,y and theta
    x = round(poseData.x, 4)
    y = round(poseData.y, 4)
    theta = round(poseData.theta, 4)
    #Save the positions in an array
    currentPose = [x, y, theta]
    #Call the add noise function.
    noisyPose = add_noise(currentPose)
    poseMsg = Pose()
    poseMsg.x = round(noisyPose[0],4)
    poseMsg.y = round(noisyPose[1],4)
    poseMsg.theta = round(noisyPose[2],4)
    pub.publish(poseMsg) #Publish msg


def add_noise(currentPose):
    xNoise = currentPose[0] + random.uniform(-SD[0],SD[0])
    yNoise = currentPose[1] + random.uniform(-SD[1],SD[1])
    thetaNoise = currentPose[2] + random.uniform(-SD[2],SD[2])
    return [xNoise, yNoise, thetaNoise]
    #Noisy data calculated at x
    #Noisy data calculated at y
    #Noisy data calculated at theta

if __name__ == '__main__':
    rospy.init_node('Turtle_Noise', anonymous = True)
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback) #Subscribe to the topic "/turtle1/pose" to read the turtle coordinates
    pub = rospy.Publisher('/Turtle_Noise', Pose, queue_size=10) #Publish the New Noisy message
    rospy.spin()