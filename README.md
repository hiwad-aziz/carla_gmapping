# GMapping with CARLA
A collection of scripts to use the output of a Lidar sensor from the CARLA simulator with the ROS gmapping package.
Radar sensor support is currently under development.
## Instructions
 - Clone https://github.com/hiwad-aziz/carla_ros_control_ego and follow steps 1-4 from the repository's instructions.
 - Install the dependencies in the running docker image:
  `sudo apt-get update`
  `sudo apt install -y ros-melodic-slam-gmapping ros-melodic-pointcloud-to-laserscan`
  
 - Add a Lidar sensor to the ego vehicle using the provided script:
 `python add_lidar.py`
 
 - Launch the pointcloud_to_laserscan package to convert the output of CARLA's Lidar sensor to the appropiate message type for gmapping:
 `roslaunch pcl_to_ls.launch`
 Parameters in the launch file can be tweaked to improve the result or modify topic names. Currently, the min and max height for sampling are set such that the ground as well as the top of the vehicle from the CARLA pointcloud are not considered. Other sensor post-processing techniques can also be applied to filter ground and ego vehicle detections.
 
 - Run gmapping:
 `rosrun gmapping slam_gmapping scan:=/laser_scan _base_frame:=ego_vehicle _map_update_interval:=0.5`
 The map will be published under the /map topic and can be visualized in rviz.

## References and links
 Gmapping docs: http://wiki.ros.org/gmapping
 Pointcloud-to-laserscan docs: http://wiki.ros.org/pointcloud_to_laserscan
 
