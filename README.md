
# GMapping with CARLA
A collection of scripts to use the output of a Lidar or Radar sensor from the CARLA simulator with the ROS gmapping package. Due to the nature of the Radar sensor, the resulting map will be more prone to errors compared to the Lidar sensor.
## Instructions
 - Clone https://github.com/hiwad-aziz/carla_ros_control_ego and follow steps 1-4 from the repository's instructions.
 - Install the dependencies in the running docker image:
  `sudo apt-get update`
  For Lidar support:
  `sudo apt install -y ros-melodic-slam-gmapping ros-melodic-pointcloud-to-laserscan`
  For Radar support:
  `sudo apt install -y ros-melodic-slam-gmapping ros-melodic-ainstein-radar-filters`
  If you want to visualize the output of CARLA's Radar sensor in rviz, you need to install the `ros-melodic-ainstein-rviz-plugins` package as well.
  
 - Add a Lidar or Radar sensor to the ego vehicle using the provided script:
 `python add_lidar.py` or `python add_radar.py`
 Parameters in the python scripts can be tweaked to modify the sensor properties.
 
 - Launch the pointcloud_to_laserscan or radar_target_array_to_laser_scan_node to convert the output of CARLA's Lidar or Radar sensor to the appropiate message types for gmapping:
 `roslaunch pcl_to_ls.launch` or `roslaunch ainstein_to_ls.launch`
 Parameters in the launch files can be modified to improve the result or change topic names. Currently, the min and max height for Lidar output sampling are set such that the ground as well as the top of the vehicle from the CARLA pointcloud are not considered. Other sensor post-processing techniques can also be applied to filter ground and ego vehicle detections.
 
 - Run gmapping:
 `rosrun gmapping slam_gmapping scan:=/laser_scan _base_frame:=ego_vehicle _map_update_interval:=0.5`
 The map will be published under the /map topic and can be visualized in rviz.

## References and links
 Gmapping docs: http://wiki.ros.org/gmapping
 Pointcloud-to-laserscan docs: http://wiki.ros.org/pointcloud_to_laserscan
 Ainstein radar filters docs: https://wiki.ros.org/ainstein_radar_filters
 
