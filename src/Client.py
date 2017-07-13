#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import socket
import json
import FileHandler
import os
import tc
import TempGen


class ClientNetworkConnector:

    gm = False

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = input(tc.align_string("Enter the IP Address of the Server: ", 3))
        self.port = int(input(tc.align_string("Enter the Port to connect to: ", 3)))
        self.real_name = input(tc.align_string("Enter your real name: ", 3))
        self.connect(self.host, self.port)
        print(tc.align_string("[INFO] Connection successful!!!", 5))
        if input(tc.align_string("Are you the GameMaster [Y]es/[N]o ?: ", 3)).upper()[0] == "Y":
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
    client = ClientNetworkConnector()
    print("\n", tc.align_string("Waiting for other Clients...", 3))
    while True:
        msg = client.receivemessage()
        try:
            msg = json.loads(msg)
            if msg["$ALL_CONN"] is True:
                break
        except json.JSONDecodeError:
            pass
    print("\n", tc.align_string("All clients connected!", 3), "\n")
    namedict = {
        "$NAME": client.real_name,
        "$GAMEMASTER": client.gm,
        "@RECIPIENT": "@SERVER",
        "$TYPE": "$FD_MATCH",
    }

    client.sendmessage(json.dumps(namedict))

    # if client.gm is True:
    #     basics = FileHandler.loadbasics()
    #     basics["$GAMEMASTER"] = client.real_name
    #     input(tc.align_string("Press ENTER to send basic information..."))
    #     client.sendmessage(json.dumps(basics, ensure_ascii=False))
    #     input(tc.align_string("Press ENTER to reload...", 3))
    #     reload_ui(basics=basics, client)
    # elif client.gm is False:
    #     basics = json.loads(client.receivemessage())
    #     print(tc.align_string("Received basic Information", 3))
    #     input(tc.align_string("Press ENTER to reload...", 3))
    #     reload_ui(basics=basics)

    return client


def reload_ui(basics: dict, client: ClientNetworkConnector):
    if client.gm is True:
        tc.create_header(text=basics["$RP_NAME"] + " by " + basics["$RP_AUTHOR"] + "   -   GameMaster", clearterm=True)
    else:
        tc.create_header(text=basics["$RP_NAME"] + " by " + basics["$RP_AUTHOR"] + " - ClientVersion", clearterm=True)
    if tc.set_term_title(basics["$RP_NAME"]) is False:
        tc.print_warning("Terminal title could not be set!")


def dist_rec_game_files(client: ClientNetworkConnector):
    if client.gm is True:
        input("\n" + tc.align_string("Press ENTER to send GameData...", 3))
        client.sendmessage(combine_json_files())
        print(tc.align_string("GameData encoded and sent...", 3))
        input()

    if client.gm is False:
        print("\n" + tc.align_string("Waiting for GameData...", 3))
        gamedatadict = json.loads(client.receivemessage())
        print(tc.align_string("GameData received... Processing...", 3))
        write_to_json_files(gamedatadict)
        input()


def combine_json_files(path: str="../GameData/"):
    gamefiledict = {}
    for folder in os.listdir(path):
        filelist = FileHandler.create_file_list(path + folder)
        gamefiledict[folder] = filelist
    sendobj = {}
    for folder, filelist in gamefiledict.items():
        for item in filelist:
            ident = path + folder + "/" + item
            with open(ident, "r") as file:
                sendobj[ident] = json.loads(file.read())
    sendobj["$DIRLIST"] = FileHandler.loaddetailfromfile("MANIFEST.json", "$DIRLIST")
    sendstr = json.dumps(sendobj, ensure_ascii=False, sort_keys=True)
    return sendstr


def write_to_json_files(filedict: dict):
    TempGen.cleargamedata()
    os.mkdir("../GameData")
    for folder in filedict["$DIRLIST"]:
        os.mkdir("../GameData/" + folder)
    for key, value in filedict.items():
        if key[0] == ".":
            with open(key, "w") as file:
                file.write(json.dumps(value, indent=2, ensure_ascii=False))


blup = client_startup()