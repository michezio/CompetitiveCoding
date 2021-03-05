COLOR = {
    "#": color(150,75,0),
    "~": color(0,128,255),
    "*": color(255,0,0),
    "+": color(128,128,128),
    "X": color(255,0,255),
    "_": color(0,255,0),
    "H": color(255,128,0),
    "T": color(0),
}

class Grid:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pixels = []
        for y in range(h):
            self.pixels.append([])
    
    def setLine(self, num, string):
        for c in string:
            self.pixels[num].append(COLOR[c])
        

def setup():
    size(1000,1000)
    global grid
    with open("5_oceania.txt", "r") as input:
        w = 500
        h = 500
        linenumber = 0
        for string in input:
            if linenumber == 0:
                s = string.split(" ")
                w = int(s[0])
                h = int(s[1])
                grid = Grid(w, h)
            elif linenumber > h:
                break
            else:
                grid.setLine(linenumber-1, string.strip())
            linenumber += 1
        
def draw():
    for y in range(grid.height):
        for x in range(grid.width):
            set(x, y, grid.pixels[y][x])
    
    noLoop()
                
                
                
                
                
                
                
