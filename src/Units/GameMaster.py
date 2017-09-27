#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


class GameMaster(Units.Unit.Unit):

    def help(self):
        print("Available actions:")
        for command in self.location.available_commands():
            print(command.name)

    def distribute_items(self):
        pass
