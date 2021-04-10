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
        self.potential = 0.0
        self.update(remaining=days)

        # self.avgscore = self.totalscore / self.numbooks
        # self.potential = (self.avgscore * self.scanperday) / self.signuptime

    def update(self, remaining):
        time = remaining - self.signuptime
        if time <= 0:
            self.potential = 0
            return
        booksToScan = time * self.scanperday
        for i in range(0, booksToScan):
            if i >= len(self.books):
                break
            self.totalscore += booklist[i].score
        # self.potential = self.totalscore
        self.potential = self.totalscore / self.signuptime

    def remBooks(self, chosen):
        for b in chosen.books:
            if b in self.books:
                self.books.remove(b)
    
    def discardBook(self, remaining):
        scannable = (remaining - self.signuptime) * self.scanperday
        if scannable >= len(self.books):
            return
        self.books = self.books[0:scannable] if scannable > 0 else self.books[0:1]


def iterateList(librarylist):
    finalList = []
    totalTime = 0
    print("LIBRERIE DA 2: {}".format(len([x for x in librarylist if x.signuptime==2])))
    while (totalTime <= days and librarylist):
        print("{} remaining, total time: {}".format(
            len(librarylist), totalTime))
        librarylist.sort(key=lambda x: (-x.potential))
        chosen = librarylist.pop(0)
        chosen.discardBook(remaining=(days-totalTime))
        for lib in librarylist:
            lib.remBooks(chosen)
            if not lib.books:
                librarylist.remove(lib)
            else:
                lib.update(remaining=(days-totalTime))
        finalList.append(chosen)
        totalTime += chosen.signuptime

    return finalList


def calculateScore(finalList):
    for lib in finalList:
        for book in lib.books:
            booklist[book].scanned = True
    score = 0
    for book in booklist:
        if book.scanned:
            score += book.score
    return score

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
    
    score = calculateScore(final)
    print("FINAL SCORE: {}".format(score))


if __name__ == "__main__":
    main_run()
