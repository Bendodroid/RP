#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]

import Units.Unit
import Engine.LocationHandler


class Player(units.unit.Unit):
    def __init__(self, *args):
        super().__init__(*args)
        self.turn_ended = False

    def help(self):
        print("Available actions:")
        for command in self.location.available_commands():
            print(command.name)

    def attack(self, target):
        target.health -= self.attack_damage
        if target.health <= 0:
            target.is_alive = False
            print(target.kill_text())
        if self.location.name == "dungeon":
            self.location.connections.append(Engine.LocationHandler.LocationHandler.generate_dungeon())
        else:
            print("You attack the {} and do {} damage.".format(target.name, self.attack_damage))

    def status(self):
        status = "Health: " + self.health + "\n "
        print(status)

    def print_inventory(self):
        inventory = "Your inventory contains:\n"
        for item in self.inventory:
            inventory += item.name + "\n"
        print(inventory)

    def walk(self):
        msg = "Locations you can go to from here:\n"
        for location_id in self.location.connections:
            msg += engine.location_handler.LocationHandler.get_location_by_id(location_id).name + "\n"
        print(msg)

        location_name = input("Where do you want to go? ").lower()
        for location_id in self.location.connections:
            location = Engine.LocationHandler.LocationHandler.get_location_by_id(location_id)
            if location_name == location.name:
                self.location = location
                print(location.text())

    def execute_command(self, command, **kwargs):
        command_func = getattr(self, command.func.__name__)
        if command_func:
            if command.ends_turn:
                self.turn_ended = True
            command_func(**kwargs)
