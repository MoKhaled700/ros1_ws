for Object Detection (it has both object detection alone and object detection with depth estimation):
	yolov5_ros
		custom msgs: detection_msgs
    links:
    	1- https://github.com/mats-robotics/yolov5_ros
    	2- https://medium.com/@jithin8mathew/estimating-depth-for-yolov5-object-detection-bounding-boxes-using-intel-realsense-depth-camera-a0be955e579a 

for Face Detection (it has both face detection alone and face detection with depth estimation):
	face_recognition
		custom msgs: Face_msgs
    links:
    	1- https://robu.in/real-time-face-detection-using-raspberry-pi-connections-and-code/
    	2- https://github.com/RishabhMalviya/face_recognition_ros_wrapper

**NOTE** for face and object recognition with depth estimation you have to launch camera first using : roslaunch realsense2_camera rs_camera.launch 

for Robot face & speech generation:
	MAIN -it has the face integrated with speech generation- : rodney_voce_test
	homer_robot_face
	homer_tts
	speech
    links:
    	1-https://github.com/homer-robotics/homer_robot_face
    	2-https://www.codeproject.com/Articles/1259980/Rodney-A-Long-Time-Coming-Autonomous-Robot-Part-5

for voice recognition:
	roboticarts_voice_control
    links:
    	1-https://github.com/RoboticArts/roboticarts_voice_control

for full body urdf:
	description

for launching rviz and automating it:
	moveit_configurations
	
    Link For neck and arms:
    For urdf and moveit setup assistant:
    	1- http://wiki.ros.org/urdf/XML/joint
    	2- https://www.youtube.com/watch?v=wobiIWrOr_s
    	3- https://www.youtube.com/watch?v=DZB5_4JCS0A&t=366s
    	4- https://youtu.be/oRd7dPLYww0
    	5- https://youtu.be/QdzmMRXAks4
    	6- https://youtu.be/K09E-_2M-vQ
    	
 for navigation and mapping: 
 
	rqt_robot_steering--> direct control on robot wheels(sending different cmd_vel) 
	rosrun rqt_robot_steering rqt_robot_steering
	------------------------------------------------------------------------------------------------------------------
	differential drive:
	We took only diff_tf_navigation python file that was used in mybot.launch but other than it we used that python script that was edited in navstack_pub src folder
	the usage of this package is to subscribe right and left ticks and publish odom and it also gives tf between odom and base footprint
	and it gives odom covarience to robot_pose_ekf
	diff_tf_navigation.py in navstack src folder: without tf transformation
	diff_tf_navigation.py in differential_drive src folder: with tf transformation
	--------------------------------------------------------------------------------------------------------------------
	robot_pose_ekf:
	this package is used to subscribe odom and imu data and publish odom_combined
	it gives tf transformation between odom and base_footprint
	--------------------------------------------------------------------------------------------------------------------
	depthimage_to_laserscan:
	this package converts depth or pointcloud of kinect camera to laser scan 
	--------------------------------------------------------------------------------------------------------------------
	Serial:
	used in communication between arduino and ros
	--------------------------------------------------------------------------------------------------------------------
	Localization_data_pub:
	this package is mentioned in automatic addison steps 
	it was used in bot.launch file in navstack_pub launch folder but this launch file was giving glitches in rviz visualization.
	it can be used instead of python file of differential_drive to subscribe right and left ticks and publish odom
	--------------------------------------------------------------------------------------------------------------------
	mpu6050_serial_to_imu:
	to increase connection duration of imu with arduino increase fifo buffer of imu that is placed in arduino code inside the package
	--------------------------------------------------------------------------------------------------------------------
	navstack_pub:
	this package is for Navigation 
	maps folder:
	conatin different maps that were token in hospital with lidar or kinect 
	src folder:
	diff_tf_navigation.py: without tf transformation
	trygoal2.py: send coordinates of object that is detected by intelrealsense camera to movebase goal 
	face.py:send coordinates of person face that is detected by intelrealsense camera to movebase goal 
	urdf folder:
	bot.urdf-> urdf lower part including kinect and imu only
	robot.urdf->urdf lower part including kinect ,imu and camera_link of intelrealsense camera
	full_robot.urdf-> urdf full body integrating with upper part (might make an error while launching moveit arm)
	different parameters folder:
	any folder that is named as param (like param_aa:parameters of automatic addison) and config 


    LINKS MIGHT HELP:
    	1- https://automaticaddison.com/how-to-control-a-robots-velocity-remotely-using-ros/?fbclid=IwAR3hZyjTrn9ihK0-LmXx7QK-PYPSpFdux_KVq_Hfi7RCQfdhvmiQJTzVmME
    	2- http://wiki.ros.org/depthimage_to_laserscan
    	3- http://wiki.ros.org/openni_launch
    	4- http://wiki.ros.org/openni
    	5- http://wiki.ros.org/differential_drive
    	6- https://github.com/fsteinhardt/mpu6050_serial_to_imu
    	7- http://wiki.ros.org/joint_state_publisher
    	8- http://wiki.ros.org/robot_state_publisher
    	9- http://wiki.ros.org/move_base
    	10- http://wiki.ros.org/map_server
    	11- http://wiki.ros.org/dwa_local_planner
    	12- http://wiki.ros.org/navfn
    	13- http://wiki.ros.org/costmap_2d


		


