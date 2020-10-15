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
  rad_bp = world.get_blueprint_library().find('sensor.other.radar')
  rad_bp.set_attribute('horizontal_fov', str(90))
  rad_bp.set_attribute('vertical_fov', str(20))
  rad_bp.set_attribute('range', str(50))
  rad_bp.set_attribute('points_per_second', str(1500))
  rad_location = carla.Location(x=3.0, z=1.0)
  rad_rotation = carla.Rotation(pitch=0)
  rad_transform = carla.Transform(rad_location,rad_rotation)
  rad_ego = world.spawn_actor(rad_bp,rad_transform,attach_to=ego_vehicle, attachment_type=carla.AttachmentType.Rigid)
