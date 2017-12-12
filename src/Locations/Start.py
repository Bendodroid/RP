#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]

import Locations.Location
import Engine.Command
import File_Handler as FH


class Start(Locations.Location.Location):
    def __init__(self, **args):
        super().__init__(**args)
        print(self.text())

    @staticmethod
    def text(self):
        return FH.load_detail(file="../GameData/09_Locations/Start.json", identifier="$TEXT")

    def update_unit(self, unit):
        pass

    def available_commands(self):
        return super().available_commands() + [Engine.Command.Status()]
