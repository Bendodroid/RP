#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import FileHandler as FH

from Functions_Client import *

from RP_Classes.SubRole import *
from RP_Classes.Items import *
from RP_Classes.Spells import *
from RP_Classes.Skills import *
from RP_Classes.Quests import *


client = client_startup()
FH.load_game_files()

while True:
    if client.gm:
        reload_ui(basics=client.basics, client=client)
        tc.print_message("Use [help] to get a list of commands", "INFO")
        execute_command(command=input("   >: "))
        input()
    else:
        pass
