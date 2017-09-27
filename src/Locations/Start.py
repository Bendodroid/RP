#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]

import Locations.Location
import FileHandler as FH


class Start(Locations.Location.Location):
    def __init__(self, **args):
        super().__init__(**args)
        print(self.text())

    def text(self):
        return FH.loaddetailfromfile(file="../GameData/09_Locations/Start.json", identifier="$TEXT")

    def update_unit(self, unit):
        pass
