import os
import sys

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
        # self.totaltime = self.signuptime + \
        #     math.ceil(self.numbooks / self.scanperday)

        self.totalscore = 0.0
        self.potential = 0.0
        self.update()

        # self.avgscore = self.totalscore / self.numbooks
        # self.potential = (self.avgscore * self.scanperday) / self.signuptime

    def update(self):
        for el in self.books:
            self.totalscore += booklist[el].score
        self.potential = self.totalscore / self.signuptime
        # for b in self.books:
        #     self.potential += float(booklist[b].score) / booklist[b].count
        # self.potential /= self.totaltime

    def remBooks(self, chosen):
        for b in chosen.books:
            if b in self.books:
                self.books.remove(b)


def iterateList(librarylist):
    finalList = []
    avgtime = 0
    for a in librarylist:
        avgtime += a.signuptime
    avgtime /= libnum
    # rimuovi quelli con signuptime maggiore della media
    # for a in librarylist:
    #     if a.signuptime > avgtime:
    #         librarylist.remove(a)
    totalTime = 0
    while (totalTime < days):
        print("{} remaining, total time: {}".format(
            len(librarylist), totalTime))
        librarylist.sort(key=lambda x: (-x.potential))
        chosen = librarylist.pop(0)
        for lib in librarylist:
            lib.remBooks(chosen)
            if not lib.books:
                librarylist.remove(lib)
            else:
                lib.update()
        finalList.append(chosen)
        totalTime += chosen.signuptime

    return finalList


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
            global booknum
            booknum = int(general[0])
            global libnum
            libnum = int(general[1])
            global days
            days = int(general[2])
            print("Libri: {}, Librerie: {}, Giorni: {}".format(
                booknum, libnum, days))
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

    final = iterateList(librarylist)

    outputFileName = "{}/{}_out.txt".format(folder, inputName)
    with open(outputFileName, "w") as out:
        out.write(str(len(final)) + "\n")
        for library in final:
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
