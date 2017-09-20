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

while True:
    if client.gm:
        reload_ui(client=client)
        tc.print_message("Use [help] to get a list of commands", "INFO")
        execute_command(command=input(FH.loaddetailfromfile(file="./MANIFEST.json", identifier="$COMM_PROMPT")))
        print("Test")
        break
    else:
        pass
