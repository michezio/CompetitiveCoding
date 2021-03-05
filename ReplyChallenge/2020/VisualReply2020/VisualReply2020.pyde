COLOR = {
    "#": color(0),
    "_": color(0,0,255),
    "M": color(255,0,0)
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
    size(600,600)
    global grid
    with open("f_glitch.txt", "r") as input:
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
                
                
                
                
                
                
                
