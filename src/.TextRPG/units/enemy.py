import units.unit

class Enemy(units.unit.Unit):
  def __init__(self, *args):
    super().__init__(*args)

class EnemySkeleton(Enemy):
  def __init__(self, location = None, attack_damage = 10, health = 20, is_alive = True):
    super().__init__("Skeleton", attack_damage, health, location, is_alive)

