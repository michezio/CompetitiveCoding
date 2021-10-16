class Piece:
    def __init__(self, line):
        u, d, l, r, *ch = line.split()
        self.char = ch[0] if len(ch) == 1 else None
        self.up = int(u)
        self.down = int(d)
        self.left = int(l)
        self.right = int(r)
        self.picked = False


with open("puzzle.txt", "r") as f:
    elements = f.read().splitlines()
    elements = elements[7:]
grid = [[None for _ in range(200)] for _ in range(200)]
'''
with open("test.txt", "r") as f:
    elements = f.read().splitlines()
grid = [[None for _ in range(4)] for _ in range(4)]
'''

pieces = [Piece(line) for line in elements]

lefts = {}
rights = {}
ups = {}
downs = {}

for i, p in enumerate(pieces):
    lefts[p.left] = i
    rights[p.right] = i
    ups[p.up] = i
    downs[p.down] = i


def connect(piece):
    if piece.picked:
        return
    piece.picked = True

    if piece.left in rights.keys():
        left = rights[piece.left]
        piece.left = pieces[left]
        #pieces[left].right = piece
    else:
        left = None
        piece.left = None

    if piece.right in lefts.keys():
        right = lefts[piece.right]
        piece.right = pieces[right]
        #pieces[right].left = piece
    else:
        right = None
        piece.right = None
    
    if piece.up in downs.keys():
        up = downs[piece.up]
        piece.up = pieces[up]
        #pieces[up].down = piece
    else:
        up = None
        piece.up = None

    if piece.down in ups.keys():
        down = ups[piece.down]
        piece.down = pieces[down]
        #pieces[down].up = piece
    else:
        down = None
        piece.down = None


for i, p in enumerate(pieces):
    #print(f"Connecting piece #{i}")
    connect(p)

currentV = None
# find top left piece
for p in pieces:
    if not p.left and not p.up:
        currentV = p
        #print("Found top-left piece!")
        break

y = 0
x = 0
while (currentV):
    currentH = currentV
    while (currentH):
        #print(f"Generating cell [{y}, {x}]")

        # the password is retrieved scanning the grid column by column
        # so here even if the values are computed horizontally they are
        # stored vertically in the grid so we have a trasposition
        grid[x][y] = currentH  
        currentH = currentH.right
        x += 1
    x = 0
    currentV = currentV.down
    y += 1

res = "".join("".join(p.char for p in row if p.char) for row in grid)
print(res)
print(res[::-1])