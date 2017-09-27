#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import Units.Player


class EventLoop():

    def __init__(self):
        self.game_ended = False
        self.comm_prompt = FH.loaddetailfromfile(file="./MANIFEST.json", identifier="$COMM_PROMPT")

    def run(self):
        while not self.game_ended:
            cmd_input = input(self.comm_prompt).lower()
            
            # valid = False
            # for command in player.location.available_commands():
            #   if cmd_input == command.name:
            #     valid = True
            #     player.execute_command(command, **command.kwargs)
            #     break
            # if not valid == True:
            #   print("{} is not a valid action.".format(cmd_input))

    # player = Units.Player.Player("Player", 10)
    # player.location = locations.start.Start()
    # while player.is_alive:
    #   player.location.update_unit(player)
    #   player.turn_ended = False
    #
    #   while player.is_alive and not player.turn_ended:
    #     cmd_input = input("C:\>").lower()
    #     valid = False
    #     for command in player.location.available_commands():
    #       if cmd_input == command.name:
    #         valid = True
    #         player.execute_command(command, **command.kwargs)
    #         break
    #     if not valid == True:
    #       print("{} is not a valid action.".format(cmd_input))
    #
    # print("You died.")
