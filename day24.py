import re
import numpy as np
import itertools


def read():
    return [line for line in open("day24.txt")]

def day24_1():
    tiles = set()
    for line in read():
        x, y = 0, 0
        sn = 0
        for char in line:
            if char == "s":
                sn = -1
            elif char == "n":
                sn = 1
            elif char == "w":
                if sn != -1:
                    x -= 1
                y += sn
                sn = 0
            elif char == "e":
                if sn != 1:
                    x += 1
                y += sn
                sn = 0
        
        if (x, y) in tiles:
            tiles.remove((x, y))
        else:
            tiles.add((x, y))

    print(len(tiles))
    return tiles


def count_ns(tiles, x, y):
    count = 0
    for dx, dy in itertools.product(range(-1, 2), repeat=2):
        if dx != dy and (x + dx, y + dy) in tiles:
            count += 1

    return count


def contains_tile(tiles, x, y):
    return any(t.is_tile(x, y) for t in tiles)


def day24_2():
    tiles = day24_1()

    for day in range(100):
        new_tiles = set()
        whites_to_check = set()

        for x, y in tiles:
            c = count_ns(tiles, x, y)
            if c == 1 or c == 2:
                new_tiles.add((x, y))

            for dx, dy in itertools.product(range(-1, 2), repeat=2):
                if dx != dy:
                    whites_to_check.add((x + dx, y + dy))

        for x, y in whites_to_check: 
            if 2 == count_ns(tiles, x, y):
                new_tiles.add((x, y))

        tiles = new_tiles

    print(len(new_tiles))

if __name__ == "__main__":
    day24_1()#382
    day24_2()#3964