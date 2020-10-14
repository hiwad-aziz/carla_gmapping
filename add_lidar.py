import carla
from carla_msgs.msg import CarlaEgoVehicleInfo

if __name__ == '__main__':
  # init carla client and world
  client = carla.Client('localhost', 2000)
  client.set_timeout(10.0)
  world = client.get_world()

  # find actor 'ego_vehicle'
  actors = world.get_actors().filter('vehicle.*')
  for actor in actors:
    if(actor.attributes.get('role_name') == 'ego_vehicle'):
      ego_id = actor.id

  ego_vehicle = world.get_actor(ego_id)

  # add lidar sensor to 'ego_vehicle'
  lidar_bp = world.get_blueprint_library().find('sensor.lidar.ray_cast')
  lidar_bp.set_attribute('channels',str(32))
  lidar_bp.set_attribute('points_per_second',str(90000))
  lidar_bp.set_attribute('rotation_frequency',str(40))
  lidar_bp.set_attribute('range',str(20))
  lidar_location = carla.Location(0,0,2)
  lidar_rotation = carla.Rotation(0,0,0)
  lidar_transform = carla.Transform(lidar_location,lidar_rotation)
  lidar_sen = world.spawn_actor(lidar_bp,lidar_transform,attach_to=ego_vehicle)
