import units.player

class Command():
  def __init__(self, name, ends_turn, func, **kwargs):
    self.name = name
    self.ends_turn = ends_turn
    self.func = func
    self.kwargs = kwargs

  def __str__(self):
    return self.name

class Help(Command):
  def __init__(self):
    super().__init__(name="help", ends_turn=False, func=units.player.Player.help)

class Status(Command):
  def __init__(slef):
    super().__init__(name="status", ends_turn=False, func=units.player.Player.status)

class Attack(Command):
  def __init__(self, target):
    super().__init__(name="attack", ends_turn=True, func=units.player.Player.attack, target=target)

class ViewInventory(Command):
  def __init__(self):
    super().__init__(name="inventory", ends_turn=False, func=units.player.Player.print_inventory)

class Walk(Command):
  def __init__(self):
    super().__init__(name="walk", ends_turn=True, func=units.player.Player.walk)
