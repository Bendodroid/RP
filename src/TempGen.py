# Copyright Bendodroid [2017]

from FileHandler import *


def createfiletemplate(folder, name="Test.json", content='{\n  "Key": "Value"\n}\n'):
    with open("../GameData/" + folder + "/" + name, "w") as file:
        file.write(content)


def cleargamedata(datapath="../GameData"):
    if os.name == "posix":
        os.system("rm -r ../GameData/")
    else:
        dirlist = os.listdir(datapath)
        combilist = []
        for folder in dirlist:
            combilist.append(create_file_list(folder))
        for filelist in combilist:
            for file in filelist:
                os.remove(file)


def createtemplates():
    arr = loaddetailfromfile("./MANIFEST.json", "$DIRLIST")
    try:
        cleargamedata()
    except OSError:
        pass
    os.mkdir("../GameData")
    for i in arr:
        os.mkdir("../GameData/" + i)
    for i in arr:
        createfiletemplate(folder=i)
    createfiletemplate("01_General", "MAIN.json",
                       json.dumps(loaddetailfromfile("./MANIFEST.json", "$TEMP_INFO"), indent=2))

createtemplates()
