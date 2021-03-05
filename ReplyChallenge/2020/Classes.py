tipo = {
    "#": 0, #muro 
    "_": 10, #developer
    "M": 5  #manager
}


class Cella:
    def __init__(self, typ, x, y):
        self.x = x
        self.y = y
        self.type = typ
        self.person = None
        self.score = 0
    
    def place(self, man):
        self.person = man 


class Mappa:
    def __init__(self, width, height, strings):
        self.width = width
        self.height = height
        self.cells = []
        for i in range(height):
            line = strings[i]
            self.cells.append([])
            for j in range(width):
                self.cells[i].append(Cella(tipo[line[j]], j, i))
        self.metric()

    def getCell(self, x, y):
        if self.inrange(y, x):
            if self.cells[y][x].type != 0:
                return self.cells[y][x]
        else:
            return None

    def inrange(self, i, j):
        return i >= 0 and i < self.height and j >= 0 and j < self.width
    
    def metric(self):
        for i in range(self.height):
            for j in range(self.width):
                score = 0
                if self.inrange(i-1, j):
                    score += self.cells[i-1][j].type
                if self.inrange(i+1, j):
                    score += self.cells[i+1][j].type
                if self.inrange(i, j-1):
                    score += self.cells[i][j-1].type
                if self.inrange(i, j+1):
                    score += self.cells[i][j+1].type
                self.cells[i][j].score = score

    def getSurrounding(self, x, y):
        ls = [
            self.getCell(x-1, y),
            self.getCell(x+1, y),
            self.getCell(x, y-1),
            self.getCell(x, y+1),
        ]
        return [x for x in ls if (x is not None and x.person is None)]

    def cellscore(self, dev, cell):
        x = cell.x
        y = cell.y

        left = self.getCell(x-1, y)
        right = self.getCell(x+1, y)
        up = self.getCell(x, y-1)
        down = self.getCell(x, y+1)

        pts = 0
        if left and left.person:
            pts += score(dev, left.person)
        if right and right.person:
            pts += score(dev, right.person)
        if up and up.person:
            pts += score(dev, up.person)
        if down and down.person:
            pts += score(dev, down.person)

        return pts
    

class Person:
    def __init__(self, id, typ):
        self.id = id
        self.type = typ
        self.company = None
        self.bonus = 0
        self.skills = set([])
        self.x = None
        self.y = None

    def place(self, cell):
        self.x = cell.x
        self.y = cell.y


class Manager(Person):
    def __init__(self, id, line):
        super().__init__(id, tipo["M"])
        par = line.split(" ")
        self.company = par[0]
        self.bonus = int(par[1])


class Developer(Person):
    def __init__(self, id, line):
        super().__init__(id, tipo["_"])
        par = line.split(" ")
        self.company = par[0]
        self.bonus = int(par[1])
        self.skills = set(par[3::])


def score(a, b):
    work_points = 0
    bonus_points = 0
    if (a.type != 2 and b.type != 2):
        intersection = len(a.skills & b.skills)
        if intersection == 0:
            return 0
        difference = len(a.skills | b.skills) - intersection
        if difference == 0:
            return 0
        work_points = intersection * difference
    if (a.company == b.company):
        bonus_points = a.bonus * b.bonus
    return work_points + bonus_points
