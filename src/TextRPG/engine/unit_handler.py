class UnitHandler():
  units = []

  @staticmethod
  def get_unit_by_id(unit_id):
    for unit in UnitHandler.units:
      if unit.unit_id == unit_id:
        return unit
