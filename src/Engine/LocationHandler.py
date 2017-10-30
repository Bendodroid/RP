#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import json

import Locations.Location
import File_Handler as FH

# import locations.dungeon
# import units.enemy


class LocationHandler:
    locations = []
    filelist = []
    datapath = FH.loaddetailfromfile(file="MANIFEST.json", identifier="$DATAPATH") + "09_Locations/"

    @staticmethod
    def get_location_by_id(location_id):
        for location in LocationHandler.locations:
            if location.location_id == location_id:
                return location

    @staticmethod
    def create_location(name, connections=None):
        if connections is None:
            connections = []
        location = Locations.Location.Location(name, connections)
        LocationHandler.locations.append(location)
        return location.location_id

    # @staticmethod
    # def generate_dungeon():
    #     dungeon = Locations.dungeon.Dungeon("dungeon", units.enemy.EnemySkeleton())
    #     dungeon.enemy.location = dungeon
    #     LocationHandler.locations.append(dungeon)
    #     return dungeon.location_id

    @staticmethod
    def generate_world():
        LocationHandler.filelist = FH.create_file_list("../GameData/09_Locations/")
        print(LocationHandler.filelist)
        with open(LocationHandler.datapath + "Cy_Te_Tendrassil.location.json", mode="r") as f:
            locobj = json.loads(f.read())
        print (locobj)
        # TODO: Klassen für Dorf, Postbox etc., je nach Info in JSON erstellen
