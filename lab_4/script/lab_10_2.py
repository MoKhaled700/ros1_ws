#!/usr/bin/env python3
import rospy
import matplotlib.pyplot as plt
import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# Create arrays for printing
XModel = []  # Array to hold value of x obtained by the sensor
YModel = []  # Array to hold value of y obtained by the sensor
ThetaModel = []  # Array to hold value of theta obtained by the sensor
XNoisy = []  # Array to hold noisy value of x coordinates
YNoisy = []  # Array to hold noisy value of y coordinates
ThetaNoisy = []  # Array to hold noisy value of theta coordinates
XFiltered = []  # Array to hold Filtered value of x coordinates
YFiltered = []  # Array to hold Filtered value of y coordinates
ThetaFiltered = []  # Array to hold Filtered value of theta coordinates
P = [[100, 0, 0], [0, 100, 0], [0, 0, 1]]
Q = [[0.01, 0, 0], [0, 0.01, 0], [0, 0, 0.01]]
R = 0.1  # Error co-variance matrix P (3x3)
U = [[0.2], [0]]
X = [[0], [0], [0]]  # Control input matrix U (3x1)
A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = [[0.1, 0], [0, 0], [0, 0.1]]
C = [[1, 0, 0]]  # State transition matrix A (3x3)
Flag_Initial = 0


def callback(Pose):
    global P, Q, R, U, X, A, B, C, Flag_Initial, Control_Input, X_updated, P_updated
    x = round(Pose.x, 4)
    y = round(Pose.y, 4)
    Theta = round(Pose.theta, 4)
    # Save the positions in an array
    position = [x, y, Theta]
    if Flag_Initial == 0:
        x_p = 5.544445
        y_p = 5.544445
        theta_p = 0
        X = [[x_p], [y_p], [theta_p]]
        Z = x_p
        # Set the states of the system
        # Set the sensor reading for the x position of the robot
        (Xpredicted, Ppredicted) = kf_prediction(X, P, A, Q, B, U)
        # Get the predicted states
        (X_updated, P_updated) = kf_correction(Xpredicted, Ppredicted, C, Z, R)  # Get the corrected states
    
    if Flag_Initial == 1:
        X = X_updated
        P = P_updated
        Z = position[0]

        (Xpredicted, Ppredicted) = kf_prediction(X, P, A, Q, B, U)
        (X_updated, P_updated) = kf_correction(Xpredicted, Ppredicted, C, Z, R)
    
    Flag_Initial = 1
    XModel.append(Xpredicted.item(0))  # Array to hold value of x obtained by the sensor
    YModel.append(Xpredicted.item(1))  # Array to hold value of y obtained by the sensor
    ThetaModel.append(Xpredicted.item(2))
    # Array to hold value of theta obtained by the sensor
    XNoisy.append(position[0])
    YNoisy.append(position[1])
    ThetaNoisy.append(position[2])  # Array to hold noisy value of x coordinates
    # Array to hold noisy value of y coordinates
    # Array to hold noisy value of theta coordinates
    XFiltered.append(X_updated.item(0))
    YFiltered.append(X_updated.item(1))
    ThetaFiltered.append(X_updated.item(2))  # Array to hold Filtered value of x coordinates
    # Array to hold Filtered value of y coordinates
    # Array to hold Filtered value of theta coordinates
    Control_Input = Twist()
    Control_Input.linear.x = 0.2
    Control_Input.linear.y = 0
    Control_Input.linear.z = 0
    Control_Input.angular.x = 0
    Control_Input.angular.y = 0
    Control_Input.angular.z = 0
    pub.publish(Control_Input)


# Prediction stage in Kalman filter
def kf_prediction(Xprev, Pprev, A, Q, B, U):
    Xpredicted = np.matmul(A, Xprev) + np.dot(B, U)
    # Predicted state vector
    Ppredicted = np.matmul(A, np.matmul(Pprev, np.transpose(A))) + Q  # Predicted error co-variance matrix
    return Xpredicted, Ppredicted


# Correction stage in Kalman filter
def kf_correction(Xpredicted, Ppredicted, C, Z, R):
    CTrans = np.transpose(C)
    num = np.matmul(Ppredicted, CTrans)
    # Numerature of Kalman gain equation
    den1 = np.matmul(C, Ppredicted)
    # CMatrix * PMatrix
    den2 = np.matmul(den1, CTrans) + R
    # CMatrix * PMatrix * CMatrix^T _+ R
    den = np.matrix(den2)
    # Place denemrature in matrix form
    deninv = den.getI()
    # (CMatrix * PMatrix * CMatrix^T _+ R) Inverse
    KGain = np.matmul(num, deninv)
    # Calculate the Kalman gain
    print("KalmanGain: " + str(KGain))
    Xfiltered = Xpredicted + np.matmul(KGain, (Z - np.matmul(C, Xpredicted)))  # Estimated updated state vector
    Pfiltered = Ppredicted - np.matmul(KGain, np.matmul(C, Ppredicted))  # Estimated updated error co-variance matrix
    return Xfiltered, Pfiltered


if __name__ == '__main__':
    rospy.init_node('Turtle_Kalman', anonymous=True)
    sub = rospy.Subscriber('/Turtle_Noise', Pose, callback)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.spin()

    # Plotting of signals from sensor and noisy signals
    plt.figure(1)
    line_1 = plt.plot(XModel, 'r-', label='X-Model')
    line_2 = plt.plot(XNoisy, 'b-', label='X-Noisy')
    line_3 = plt.plot(XFiltered, 'g-', label='X-Filtered')
    plt.legend()
    plt.figure(2)
    line_1 = plt.plot(YModel, 'r-', label='Y-Model')
    line_2 = plt.plot(YNoisy, 'b-', label='Y-Noisy')
    line_3 = plt.plot(YFiltered, 'g-', label='Y-Filtered')
    plt.legend()
    plt.figure(3)
    line_1 = plt.plot(ThetaModel, 'r-', label='Theta-Model')
    line_2 = plt.plot(ThetaNoisy, 'b-', label='Theta-Noisy')
    line_3 = plt.plot(ThetaFiltered, 'g-', label='Theta-Filtered')
    plt.legend()
    plt.show(block=True)
