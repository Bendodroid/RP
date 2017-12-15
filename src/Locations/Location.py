#!/usr/bin/env python3.6

# Copyright Bendodroid [2017]

import Engine.Command


class Location:
    location_id = 0
    location_count = 0

    def __init__(self, name: str, visible: bool, description: str, region: str,
                 county: str, enable_commands: list, enable_locations: list,
                 connections: list, corr_file: str):
        self.location_id = Location.location_count
        Location.location_count += 1

        self.name = name
        self.visible = visible
        self.description = description
        self.region = region
        self.county = county
        self.enable_commands = enable_commands
        self.enable_locations = enable_locations
        self.connections = connections
        self.corr_file = corr_file

    def get_location_id(self):
        return self.location_id

    @staticmethod
    def get_description():
        raise NotImplementedError()

    def update_unit(self, unit):
        raise NotImplementedError()

    def available_commands(self):
        return [Engine.Command.Help()]
