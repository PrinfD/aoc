import re
import numpy as np
import math
import collections
import itertools

class Tile:
    singles = set()
    doubles = set()

    refs = {}

    TOP = 0
    BOTTOM = 2
    LEFT = 1
    RIGHT = 3

    def __init__(self, name, tile):
        self.id = int(name)
        
        res = []
        for line in tile:
            l = line.replace(".", "0").replace("#", "1")
            l = [x for x in l]
            res.append(l)

        self.tile = np.array(res)
        self.siblings = []

        self.bs = ["", "", "", ""]
        self.bs[Tile.TOP], self.bs[Tile.BOTTOM] = "".join(self.tile[0]), "".join(self.tile[-1])
        self.bs[Tile.LEFT], self.bs[Tile.RIGHT] = "".join(self.tile[:,0]), "".join(self.tile[:,-1])
        #todo eig auch rotieren

        self._register()

    def __str__(self):
        return str(self.id)

    def _register(self):
        for b in self.bs:
            bx = int(b, base=2)
            by = int(b[::-1], base=2)

            arr = Tile.refs.get(bx, [])
            arr.append(self)
            Tile.refs[bx] = arr

            if by != bx:
                arr = Tile.refs.get(by, [])
                arr.append(self)
                Tile.refs[by] = arr

            if bx in Tile.singles:
                Tile.doubles.add(bx)
            else:
                Tile.singles.add(bx)

            if by in Tile.singles:
                Tile.doubles.add(by)
            else:
                Tile.singles.add(by)
    
    def find_siblings(self):
        siblings = np.empty(4, dtype=object)
        for i in range(len(self.bs)):
            b = int(self.bs[i], base=2)
            if b in Tile.doubles:
                if Tile.refs[b][0].id != self.id:
                    siblings[i] = Tile.refs[b][0]
                else:
                    siblings[i] = Tile.refs[b][1]

        self.siblings = siblings
        return siblings

    def is_corner(self):
        count = len([b for b in self.siblings if b])
        return count == 2

    def rotate_corner(self):
        while self.siblings[Tile.LEFT] != None or self.siblings[Tile.TOP] != None:
            self.rotate_clockwise()

    def rotate_clockwise(self):
        tmp = self.siblings[0]
        for i in range(1, 4):
            self.siblings[i - 1] = self.siblings[i]
            self.tile = np.rot90(self.tile, k=1)
        
        self.siblings[3] = tmp

    def vflip(self):
        self.siblings[Tile.TOP], self.siblings[Tile.BOTTOM] = self.siblings[Tile.BOTTOM], self.siblings[Tile.TOP]
        self.tile = np.flipud(self.tile)
        

    def hflip(self):
        self.siblings[Tile.RIGHT], self.siblings[Tile.LEFT] = self.siblings[Tile.LEFT], self.siblings[Tile.RIGHT]
        self.tile = np.fliplr(self.tile)

    def rotate_match(self, left, top):
        if left:
            while self.siblings[Tile.LEFT] != left:
                self.rotate_clockwise()
            if self.siblings[Tile.TOP] != top: 
                self.vflip()
        else:
            while self.siblings[Tile.TOP] != top:
                self.rotate_clockwise()
            if self.siblings[Tile.LEFT] != left:
                self.hflip()

def day20():
    tiles_with_name = "".join(open("day20.txt").readlines())
    tiles_with_name = tiles_with_name.strip().split("\n\n")

    tiles = []

    for tile in tiles_with_name:
        split_tile = tile.splitlines()
        name = split_tile[0].split()[1][:-1]
        tile = split_tile[1:]

        tiles.append(Tile(name, tile))

    for c in tiles:
        c.find_siblings()

    corners = [t for t in tiles if t.is_corner()]
      
    print(math.prod((c.id for c in corners)))#66020135789767


    #day 20_2
    size = math.isqrt(len(tiles))
    aranged_tiles = np.empty((size, size), dtype=object)
    aranged_tiles[0,0] = corners[0]

    corners[0].rotate_corner()

    for y in range(size):
        for x in range(size):
            if x == 0 and y == 0:
                continue

            if x == 0:
                top = aranged_tiles[y-1,x]
                aranged_tiles[y,x] = top.siblings[Tile.BOTTOM]
                aranged_tiles[y,x].rotate_match(None, top)
            elif y == 0:
                left = aranged_tiles[y,x-1]
                aranged_tiles[y,x] = left.siblings[Tile.RIGHT]
                aranged_tiles[y,x].rotate_match(left, None)
            else:
                top = aranged_tiles[y-1,x]
                left = aranged_tiles[y,x-1]
                aranged_tiles[y,x] = left.siblings[Tile.RIGHT]
                aranged_tiles[y,x].rotate_match(left, top)

    #format_output(aranged_tiles)

    image = format_image(aranged_tiles)
    pretty_print(image, 8)
    search_snake(image)

def search_snake(ori_image):
    snake = ["00000000000000000010", "10000110000110000111", "01001001001001001000"]
    snake_one_count = sum([s.count("1") for s in snake])
    rows = []
    for row in snake:
        rows.append([True if c == "1" else False for c in row])
    snake_arr = np.array(rows)

    total = 0
    image = ori_image
    flip = True
    while total == 0:
        for y in range(len(image) - len(snake)):
            for x_offset in range(len(image[y]) - len(snake[0])):
                view = image[y:y+len(snake),x_offset:x_offset+len(snake[0])]
                
                sizey, sizex = snake_arr.shape
                match_failed = any(snake_arr[sy,x] and view[sy,x] != '1' for sy, x in itertools.product(range(sizey), range(sizex)))
                if not match_failed:
                    total += 1
        
        if total == 0:
            if flip:
                image = np.fliplr(image)
            else:
                image = np.fliplr(image)
                image = np.rot90(image)

            flip = not flip

    print(len(image[image == "1"]), total, snake_one_count)
    print(len(image[image == "1"]) - snake_one_count * total)


def format_image(aranged_tiles):
    rows = [np.hstack([t.tile[1:-1,1:-1] for t in tile_row]) for tile_row in aranged_tiles]
    return np.vstack(rows)

def format_output(aranged_tiles):
    rows = [np.hstack([t.tile for t in tile_row]) for tile_row in aranged_tiles]
    pretty_print(np.vstack(rows), 10)

def pretty_print(array2d, length):
    rowcount = 0
    x = ""
    for row in array2d:
        rowcount += 1
        count = 0
        for c in row:
            count += 1
            x += c
            if count == length:
                count = 0
                x += " "
        
        x += "\n"
        if rowcount == length:
            rowcount = 0
            x += "\n"

    print(x)


if __name__ == "__main__":
    day20()