import locations.location
import locations.dungeon
import units.enemy

class LocationHandler:
  locations = []

  @staticmethod
  def get_location_by_id(location_id):
    for location in LocationHandler.locations:
      if location.location_id == location_id:
        return location

  @staticmethod
  def create_location(name, connections = []):
    location = locations.location.Location(name, connections)
    LocationHandler.locations.append(location)
    return location.location_id

  @staticmethod
  def generate_dungeon():
    dungeon = locations.dungeon.Dungeon("dungeon", units.enemy.EnemySkeleton())
    dungeon.enemy.location = dungeon
    LocationHandler.locations.append(dungeon)
    return dungeon.location_id 
