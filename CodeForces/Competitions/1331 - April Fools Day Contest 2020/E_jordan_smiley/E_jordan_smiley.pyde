def setup():
    img = loadImage("map.png")
    arr = []
    w = img.width
    w /= 64
    off = w/2
    
    for y in range(64):
        arr.append([])
        for x in range(64):
            c = img.get(x*w + off, y*w + off)
            if (c > color(127)):
                c = 0
            else:
                c = 1
            arr[y].append(c)
    
    print(arr)
