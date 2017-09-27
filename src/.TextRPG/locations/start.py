import locations.location
import engine.location_handler
import engine.command


class Start(locations.location.Location):
    def __init__(self):
        super().__init__("start", [engine.location_handler.LocationHandler.generate_dungeon()])

    def update_unit(self, unit):
        pass

    def available_commands(self):
        return [engine.command.Help(), engine.command.Walk()]

    def text(self):
        return "Spawn"
