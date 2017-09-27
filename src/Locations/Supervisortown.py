#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]

import Locations.Location
import Engine.Command


class Supervisortown(Locations.Location.Location):

    def __init__(self, name):
        super().__init__("supervisortown", [])

    def available_commands(self):
        pass
