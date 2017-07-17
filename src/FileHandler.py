# Copyright Bendodroid [2017]


import os
import json


def create_file_list(path: str):
    filelist = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            filelist.append(f)
    return filelist


def loaddetailfromfile(file: str, identifier):
    with open(file, "r") as f:
        obj = json.loads(f.read())
        return obj[identifier]


def createjsonfile(file: str, obj):
    with open(file, "w") as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=4))


def loadbasics():
    with open("../GameData/01_General/MAIN.json", "r") as f:
        obj = json.loads(f.read())
    obj["$RECIPIENT"] = "ALL"
    return obj
