class Item:
  def __init__(self, name, base_price, description = ""):
    self.name = name
    self.base_price = base_price
    self.description = description

  def use():
    pass

class Weapon(Item):
  def __init__(self, *args, base_damage):
    super().__init__(*args)
    self.base_damage = base_damage 
