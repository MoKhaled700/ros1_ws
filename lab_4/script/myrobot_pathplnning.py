#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist, Pose
from gazebo_msgs.msg import ModelStates
from math import pow, atan2, sqrt, asin

class TurtleBot:
    def __init__(self):
        # Creating our node,publisher and subscriber
        rospy.init_node('my_robot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/gazebo/model_states', ModelStates, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type ModelStates is received by the subscriber."""
        self.pose = data.pose[-1]
        self.pose.position.x = round(self.pose.position.x, 2)
        self.pose.position.y = round(self.pose.position.y, 2)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.position.x), 2) +pow((goal_pose.y - self.pose.position.y), 2))
    
    def linear_vel_controller(self, goal_pose, k_p=1.5):
        """Linear velocity P controller"""
        if k_p * self.euclidean_distance(goal_pose) > 0.5:
            return 0.5
        else:
            return k_p * self.euclidean_distance(goal_pose)
    
    def steering_angle(self, goal_pose):
        """Calculating steering angle"""
        return atan2(goal_pose.y - self.pose.position.y, goal_pose.x - self.pose.position.x)
    
    def euler_from_quaternion(self, x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = atan2(t0, t1)
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = asin(t2)
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = atan2(t3, t4)
        return yaw_z # in radians

    def angular_vel_controller(self, goal_pose, k_p=6):
        """Angular velocity P controller"""
        theta = self.euler_from_quaternion(x = self.pose.orientation.x, y = self.pose.orientation.y, z = self.pose.orientation.z, w = self.pose.orientation.w)
        if k_p * (self.steering_angle(goal_pose) - round(theta, 4)) > 1.5:
            return 1.5
        elif k_p * (self.steering_angle(goal_pose) - round(theta, 4)) < -1.5:
            return -1.5
        else:
            return k_p * (self.steering_angle(goal_pose) - round(theta, 4))
    
    def move2goal(self, path_point_x, path_point_y):
        """Moves the robot to the goal."""
        goal_pose = Pose().position
        
        goal_pose.x = float(path_point_x)
        goal_pose.y = float(path_point_y)
        distance_tolerance = 0.1
        vel_msg = Twist()
        while self.euclidean_distance(goal_pose) >= distance_tolerance:
            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control
            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel_controller(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel_controller(goal_pose)
            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            # Publish at the desired rate.
            self.rate.sleep()
            # Stopping our robot after the movement is over.
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)



def breadth_first(map, start, goal, direction):
    queue = [start]
    explored = []
    parents = []
    goal_reached = False
    while queue:
        node = queue.pop(0)
        if node == goal:
            goal_reached = True
            break
        neighbours = get_neighbours(node, direction)
        for neighbour in neighbours:
            if neighbour not in explored and map[neighbour[0]][neighbour[1]] == 1:
                queue.append(neighbour)
                explored.append(neighbour)
                parents.append(node)
    if goal_reached:
        path= get_path(start, goal, parents, explored)
        return path
    else:
        print("Stuck")
        return []
def get_path(start, goal, parents, explored):
    path = [goal]
    node = goal
    while node != start:
        path.append(parents[explored.index(node)]) # explored.index(node) 5
        node = parents[explored.index(node)]
    path.reverse()
    print("The path is: " + str(path))
    return path

def get_neighbours(node, direction):
    neighbours = []
    if direction == 1: #CW
        neighbours.append([node[0], node[1]+1]) #node = [1, 1]
        neighbours.append([node[0]+1, node[1]+1])
        neighbours.append([node[0]+1, node[1]])
        neighbours.append([node[0] + 1, node[1] - 1])
        neighbours.append([node[0], node[1] - 1])
        neighbours.append([node[0] - 1, node[1] - 1])
        neighbours.append([node[0] - 1, node[1]])
        neighbours.append([node[0] - 1, node[1] + 1])

    if direction == -1:
        neighbours.append([node[0], node[1] + 1])
        neighbours.append([node[0] - 1, node[1] + 1])
        neighbours.append([node[0] - 1, node[1]])
        neighbours.append([node[0] - 1, node[1] - 1])
        neighbours.append([node[0], node[1] - 1])
        neighbours.append([node[0] + 1, node[1] - 1])
        neighbours.append([node[0] + 1, node[1]])
        neighbours.append([node[0] + 1, node[1] + 1])
    
    return neighbours



if __name__ == '__main__':
    Map = [[1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]]

    the_path = breadth_first(Map, [0,0], [5,5], 1) # map, start, goal, direction
    try:
        x = TurtleBot()
        for i in range(0, len(the_path)):

            x.move2goal(the_path[i][1], -the_path[i][0])
    except rospy.ROSInterruptException:
        pass