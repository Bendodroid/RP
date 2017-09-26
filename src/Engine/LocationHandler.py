#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import Locations.Location
# import locations.dungeon
# import units.enemy


class LocationHandler:
    locations = []

    @staticmethod
    def get_location_by_id(location_id):
        for location in LocationHandler.locations:
            if location.location_id == location_id:
                return location

    @staticmethod
    def create_location(name, connections = []):
        location = Locations.Location.Location(name, connections)
        LocationHandler.locations.append(location)
        return location.location_id

    # @staticmethod
    # def generate_dungeon():
    #     dungeon = Locations.dungeon.Dungeon("dungeon", units.enemy.EnemySkeleton())
    #     dungeon.enemy.location = dungeon
    #     LocationHandler.locations.append(dungeon)
    #     return dungeon.location_id
