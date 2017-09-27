import locations.location
import engine.command

class Dungeon(locations.location.Location):
  def __init__(self, name, enemy):
    super().__init__("dungeon", [])
    self.enemy = enemy

  def update_unit(self, unit):
    if self.enemy.is_alive:
      print("The {} attacks you! You take {} damage".format(self.enemy.name, self.enemy.attack_damage))
      self.enemy.attack(unit)

  def available_commands(self):
    if self.enemy.is_alive:
      return [engine.command.Help(), engine.command.Attack(self.enemy)]

    return [engine.command.Help(), engine.command.Walk()]

  def text(self):
    return "You enter a dungeon.\nYou encounter a {}!".format(self.enemy.name)
