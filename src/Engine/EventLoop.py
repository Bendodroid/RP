#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import Units.Player
import Locations.Start
import Engine.LocationHandler

import tc
import File_Handler as FH


class EventLoop:
    def __init__(self):
        self.game_ended = False
        self.comm_prompt = FH.loaddetailfromfile(file="./MANIFEST.json", identifier="$COMM_PROMPT")

    def run(self):
        # Start fresh or load saved game
        new_or_load = input(tc.align_string("[S]tart a new game or [L]oad an old one?: ", 5))
        if new_or_load[0].lower() == "s":
            player = Units.Player.Player(name="Test", level=1, max_health=100, max_attack_dmg=100,
                                         inv=[], armor_inv=[], location=None, is_alive=True)
            Engine.LocationHandler.LocationHandler.generate_world()
            
            # player.location = Locations.Start.Start(name="start")
            #
            # while player.is_alive:
            #     player.location.update_unit(player)
            #     player.turn_ended = False
            #
            #     while player.is_alive and not player.turn_ended:
            #         cmd_input = input(self.comm_prompt).lower()
            #         valid = False
            #         for command in player.location.available_commands():
            #             if cmd_input == command.name:
            #                 valid = True
            #                 player.execute_command(command, **command.kwargs)
            #                 break
            #         if valid is not True:
            #             print("{} is not a valid action.".format(cmd_input))
            # print("You died.")
        elif new_or_load[0].lower() == "l":
            print(tc.print_warning(msg="NOT IMPLEMENTED YET!"))
            print("HALLO")
