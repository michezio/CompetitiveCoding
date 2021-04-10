import os
import sys
import math

booklist = []
librarylist = []


class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False
        self.count = 0


class Library:
    def __init__(self, id, firstline, secondline):
        self.id = id
        self.numbooks = int(firstline[0])
        self.signuptime = int(firstline[1])
        self.scanperday = int(firstline[2])
        self.books = [int(x) for x in secondline]
        for b in self.books:
            booklist[b].count += 1
        self.books.sort(key=lambda x: booklist[x].score, reverse=True)
        self.totaltime = self.signuptime + \
            math.ceil(self.numbooks / self.scanperday)

        self.totalscore = 0.0
        for el in self.books:
            self.totalscore += booklist[el].score
        self.avgscore = self.totalscore / self.numbooks

        # self.potential = (self.avgscore * self.scanperday) / self.signuptime
        self.potential = self.totalscore / self.totaltime

    def updatePotential(self):
        self.potential = 0.0
        for b in self.books:
            self.potential += float(booklist[b].score) / booklist[b].count
        self.potential /= self.totaltime


def main_run():

    arguments = [x.lower() for x in sys.argv[1::]]
    if len(arguments) == 0:
        print("PLEASE SPECIFY A FILE")
        exit()
    else:
        inputName = arguments[0]

    folder = ("output/")
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        with open("input/{}.txt".format(inputName), "r") as inputFile:
            general = inputFile.readline().split(" ")
            # booknum = int(general[0])
            libnum = int(general[1])
            # days = int(general[2])
            bookline = inputFile.readline().split(" ")
            i = 0
            for score in bookline:
                booklist.append(Book(i, int(score)))
                i += 1
            for i in range(0, libnum):
                libline = inputFile.readline().split(" ")
                libbooks = inputFile.readline().split(" ")
                librarylist.append(Library(i, libline, libbooks))
    except IOError:
        print("!!! {}.txt NOT FOUND IN INPUT FOLDER !!!".format(inputName))
        exit()

    # for lib in librarylist:
    #     lib.updatePotential()

    librarylist.sort(key=lambda x: (x.signuptime))

    outputFileName = "{}/{}_out.txt".format(folder, inputName)
    with open(outputFileName, "w") as out:
        out.write(str(len(librarylist)) + "\n")
        for library in librarylist:
            for book in library.books:
                lastbook = book
                if booklist[book].scanned is True:
                    library.books.remove(book)
                if not library.books:
                    library.books.append(lastbook)
            out.write(str(library.id) + " " + str(len(library.books)) + "\n")
            for book in library.books:
                out.write(str(book) + " ")
                booklist[book].scanned = True
            out.write("\n")


if __name__ == "__main__":
    main_run()
