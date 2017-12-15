#!/usr/bin/env python3.6

# Copyright Bendodroid [2017]

import Locations.Location as Locations
import Engine.Command
import File_Handler as FH


class Start(Locations.Location):

    def __init__(self, **args):
        super().__init__(**args)
        print(self.get_description())

    @staticmethod
    def get_description():
        return FH.load_detail(file="../GameData/09_Locations/Cy_Te_Tendrassil.location.json",
                              identifier="$DESCRIPTION")

    def update_unit(self, unit):
        pass

    def get_available_commands(self):
        return super().available_commands() + [Engine.Command.Status()]
