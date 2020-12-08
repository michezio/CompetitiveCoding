import os
import sys
import math
from Classes import Mappa, Developer, Manager
import algo1 as Solve


def main_run():

    arguments = [x.lower() for x in sys.argv[1::]]
    if len(arguments) == 0:
        print("PLEASE SPECIFY A FILE")
        exit()
    else:
        inputName = arguments[0]
    
    print(inputName)

    folder = ("output/")
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        with open("input/{}.txt".format(inputName), "r") as inputFile:
            dim = inputFile.readline().split(" ")
            strings = []
            for i in range(int(dim[1])):
                strings.append(inputFile.readline().strip())
            print(strings)
            global mappa
            mappa = Mappa(int(dim[0]), int(dim[1]), strings)

            print("Larghezza: {}, Altezza: {}".format(mappa.width, mappa.height))
            for r in mappa.cells:
                for c in r:
                    print(c.type)

            global devs
            devs = []
            dev_num = int(inputFile.readline().strip())
            for i in range(dev_num):
                devs.append(Developer(i, inputFile.readline()))
            
            global managers
            managers = []
            man_num = int(inputFile.readline().strip())
            for i in range(man_num):
                managers.append(Manager(i, inputFile.readline()))

            print("Developers: {}, Managers: {}".format(len(devs), len(managers)))
    except IOError:
        print("!!! {}.txt NOT FOUND IN INPUT FOLDER !!!".format(inputName))
        exit()

    Solve.run(mappa, devs, managers)

    devs.sort(key=lambda x: x.id)
    managers.sort(key=lambda x: x.id)

    outputFileName = "{}/{}_out.txt".format(folder, inputName)
    with open(outputFileName, "w") as out:
        for d in devs:
            if d.x:
                out.write(str(d.x) + " " + str(d.y) + "\n")
            else:
                out.write("X\n")


if __name__ == "__main__":
    main_run()
