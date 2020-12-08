class Comp:
    def __init__(self, name):
        self.name = name
        self.devlist = []
        self.manlist = []


def run(mappa, devs, mans):

    companies = {}
    for d in devs:
        if (d.company not in companies):
            companies[d.company] = Comp(d.company)
        companies[d.company].devlist.append(d)
    for m in mans:
        companies[m.company].manlist.append(m)

    biggest_companies = [k[1] for k in sorted(companies.items(), key=lambda item: -len(item[1].devlist))]

    for c in biggest_companies:
        c.manlist.sort(key=lambda x: -x.bonus)
        c.devlist.sort(key=lambda x: -(x.bonus*len(x.skills)))

    best_cells = []
    for r in mappa.cells:
        for cel in r:
            best_cells.append(cel)
    
    best_cells = [x for x in best_cells if x.type == 5]
    best_cells.sort(key=lambda x: -x.score)

    mans.sort(key=lambda x: -x.bonus)

    for i in range(min(len(mans), len(best_cells))):
        c = best_cells[i]
        mans[i].place(c)
        c.place(mans[i])

    next_cells = best_cells
    while (next_cells):
        done_cells = next_cells
        next_cells = []    
        for c in done_cells:
            x = c.x
            y = c.y
            for cell in mappa.getSurrounding(x, y):
                best_dev = None
                best_score = 0
                for d in devs:
                    if d.x:
                        continue
                    score = mappa.cellscore(d, cell)
                    if score >= best_score:
                        best_score = score
                        best_dev = d
                if best_dev:
                    cell.place(best_dev)
                    best_dev.place(cell)
                    next_cells.append(cell)
