#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import socket
import json
import FileHandler as FH
import os
import tc
import TempGen


class ClientNetworkConnector:

    gm = False
    peers = []
    gm_peer = str()
    basics = {}
    commands = []

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = input(tc.align_string("Enter the IP Address of the Server: ", 3))
        self.port = int(input(tc.align_string("Enter the Port to connect to: ", 3)))
        self.real_name = input(tc.align_string("Enter your real name: ", 3))
        self.connect(self.host, self.port)
        print(tc.print_message("Connection successful!!!", "INFO"))
        if input("\n" + tc.align_string("Are you the GameMaster [Y]es/[N]o ?: ", 3)).upper()[0] == "Y":
            self.gm = True

    def connect(self, host, port):
        self.s.connect((host, port))

    def disconnect(self):
        self.s.close()

    def sendmessage(self, msg):
        self.s.sendall(msg.encode("utf-8"))

    def receivemessage(self):
        msg = None
        while not msg:
            msg = self.s.recv(1024).decode("utf-8")
        return msg


###


def client_startup():
    tc.create_header(text="RP-API by Bendodroid - Client Version", clearterm=True)
    tc.set_term_title("RP-API - Client")

    client = ClientNetworkConnector()

    print(tc.print_message("Waiting for other Clients...", "INFO"))
    while True:
        msg = client.receivemessage()
        try:
            msg = json.loads(msg)
            if msg["$ALL_CONN"] is True:
                break
        except json.JSONDecodeError:
            pass

    print(tc.print_message("All clients connected!", "INFO"))

    # Send Info
    namedict = {
        "$NAME": client.real_name,
        "$GAMEMASTER": client.gm,
        "$RECIPIENT": "SERVER",
        "$TYPE": "FD_MATCH",
    }
    client.sendmessage(json.dumps(namedict))

    # Receive Info on other Clients
    print(tc.print_message("Waiting for information on other peers...", "INFO"))
    peerinfo = json.loads(client.receivemessage())
    client.peers = []
    for key, value in peerinfo["name_fd_match"].items():
        client.peers.append(key)
    client.gm_peer = peerinfo["gamemaster"]
    print(tc.print_message("Successful!", "INFO"))

    if client.gm:
        basics = FH.loadbasics()
        input(tc.print_message("Press ENTER to send basic information...", "INFO"))
        client.sendmessage(json.dumps(basics, ensure_ascii=False))
    else:
        print(tc.print_message("Waiting for basic information...", "INFO"))
        basics = json.loads(client.receivemessage())
        print(tc.print_message("Received basic information!", "INFO"))

    input(tc.print_message("Press ENTER to reload...", "INFO"))
    client.basics = basics
    reload_ui(client=client)
    dist_rec_game_files(client=client)
    load_commands(client=client)
    return client


def reload_ui(client: ClientNetworkConnector):
    if client.gm is True:
        tc.create_header(text=client.basics["$RP_NAME"] + " by " + client.basics["$RP_AUTHOR"] + " - GameMaster",
                         clearterm=True)
    else:
        tc.create_header(text=client.basics["$RP_NAME"] + " by " + client.basics["$RP_AUTHOR"] + " - ClientVersion",
                         clearterm=True)
    if tc.set_term_title(client.basics["$RP_NAME"]) is False:
        tc.print_warning("Terminal title could not be set!")


def dist_rec_game_files(client: ClientNetworkConnector):
    if client.gm is True:
        input(tc.print_message("Press ENTER to send GameData...", "INFO"))
        client.sendmessage(combine_json_files())
        print(tc.print_message("GameData encoded and sent...", "INFO"))

    if client.gm is False:
        print(tc.print_message("Waiting for GameData...", "INFO"))
        gamedatadict = json.loads(client.receivemessage())
        print(tc.print_message("GameData received... Processing...", "INFO"))
        write_to_json_files(gamedatadict)
        print(tc.print_message("GameData is up to date!", "INFO"))


def combine_json_files(path: str="../GameData/"):
    gamefiledict = {}
    for folder in os.listdir(path):
        filelist = FH.create_file_list(path + folder)
        gamefiledict[folder] = filelist
    sendobj = {}
    for folder, filelist in gamefiledict.items():
        for item in filelist:
            ident = path + folder + "/" + item
            with open(ident, "r") as file:
                sendobj[ident] = json.loads(file.read())
    sendobj["$DIRLIST"] = FH.loaddetailfromfile("MANIFEST.json", "$DIRLIST")
    sendobj["$RECIPIENT"] = "ALL"
    sendstr = json.dumps(sendobj, ensure_ascii=False, sort_keys=True)
    return sendstr


def write_to_json_files(datadict: dict):
    TempGen.cleargamedata()
    os.mkdir("../GameData")
    for folder in datadict["$DIRLIST"]:
        os.mkdir("../GameData/" + folder)
    for key, value in datadict.items():
        if key[0] == ".":
            with open(key, "w") as file:
                file.write(json.dumps(value, indent=2, ensure_ascii=False))


def load_commands(client: ClientNetworkConnector):
    commands = FH.loaddetailfromfile("../GameData/01_General/MAIN.json", "$GM_COMMAND_LIST")
    for pair in commands:
        client.commands.append(Command(long_comm=pair[0], short_comm=pair[1]))
    print(client.commands)


def execute_command(command: str):
    pass
    #if command.lower() == ""
