#!/usr/bin/env python3.6

# Copyright Bendodroid [2017]


import json
import typing

import Locations.Location as Locations
# import Units.Player as Units
import File_Handler as FH

# import locations.dungeon
# import units.enemy


class LocationHandler:
    locations: typing.List[Locations.Location] = []
    datapath: typing.AnyStr = ""
    loc_filelist: typing.List = []
    start_loc: typing.AnyStr = ""

    @staticmethod
    def update_Handler():
        root_path = FH.load_detail(file="MANIFEST.json", identifier="$DATAPATH")
        loc_path = FH.load_detail(file="MANIFEST.json", identifier="$DATAPATH_LOCATIONS")
        LocationHandler.datapath = root_path + loc_path
        LocationHandler.loc_filelist = FH.create_file_list(LocationHandler.datapath)
        LocationHandler.start_loc = FH.load_detail(file="MANIFEST.json", identifier="$START_LOC")

    @staticmethod
    def get_location_by_id(location_id):
        for location in LocationHandler.locations:
            if location.location_id == location_id:
                return location

    @staticmethod
    def create_location(*args):
        location = Locations.Location(*args)
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
        print(LocationHandler.loc_filelist)
        # Generate Location-Objects
        for foo in LocationHandler.loc_filelist:
            print(foo)
            with open(LocationHandler.datapath + foo, mode="r") as f:
                locobj = json.loads(f.read())
            LocationHandler.create_location(locobj["$NAME"], locobj["$VISIBLE"], locobj["$DESCRIPTION"],
                                            locobj["$REGION"], locobj["$COUNTY"], locobj["$ENABLE_COMMANDS"],
                                            locobj["$ENABLE_LOCATIONS"], locobj["$CONNECTIONS"], foo)

        # Update Connections
        for locobj in LocationHandler.locations:
            for conn_str in locobj.connections:
                for connobj in LocationHandler.locations:
                    if connobj.corr_file == conn_str:
                        locobj.connections[locobj.connections.index(conn_str)] = connobj.get_location_id()

        # Debug Connections
        for i in LocationHandler.locations:
            for j in i.connections:
                print(i.corr_file, " : ", j)

    @staticmethod
    def place_player_start(playerobj):
        for loc in LocationHandler.locations:
            if loc.corr_file == LocationHandler.start_loc:
                playerobj.location = loc
