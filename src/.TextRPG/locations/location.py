import engine.command


class Location:
    location_id = 0
    location_count = 0

    def __init__(self, name, connections=[]):
        self.location_id = Location.location_count
        Location.location_count = Location.location_count + 1

        self.name = name
        self.connections = connections

    def text(self):
        raise NotImplementedError()

    def update_unit(self, unit):
        raise NotImplementedError()

    def available_commands(self):
        return [engine.command.Help(), engine.command.Walk()]
