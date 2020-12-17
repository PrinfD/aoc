import re
import numpy as np


def read():
    return [line for line in open("day17.txt")]

def char_to_bool(c):
    return c == "#"

def in_range(v, r):
    return 0 <= v < r

def neig_count(w, x, y, z, pocket_dim):
    count = 0
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                for dw in range(-1, 2):
                    if dw != 0 or dx != 0 or dy != 0 or dz != 0:
                        if in_range(z + dz, len(pocket_dim)) and in_range(y + dy, len(pocket_dim[z+dz])) and in_range (x + dx, len(pocket_dim[z+dz][y+dy])) and in_range (w + dw, len(pocket_dim[z+dz][y+dy][x+dx])):
                            if pocket_dim[z + dz][y + dy][x + dx][w + dw]:
                                count += 1
    return count

def total(pocket_dim):
    total = 0
    for z in pocket_dim:
        for y in z:
            for x in y:
                for w in x:
                    if w:
                        total += 1
    return total


def is_active(w, x, y, z, pocket_dim):
    return in_range(z, len(pocket_dim)) and in_range(y, len(pocket_dim[z])) and in_range(x, len(pocket_dim[z][y])) and in_range(w, len(pocket_dim[z][y][x])) and pocket_dim[z][y][x][w]


def expand_dim(pocket_dim):
    next_cycle = np.zeros([len(pocket_dim)+2, len(pocket_dim[0])+2, len(pocket_dim[0][0])+2, len(pocket_dim[0][0][0])+2], dtype=bool)

    for z in range(len(next_cycle)):
        for y in range(len(next_cycle[z])):
            for x in range(len(next_cycle[z][y])):
                for w in range(len(next_cycle[z][y][x])):
                    count = neig_count(w-1, x-1, y-1, z-1, pocket_dim)
                    if count == 3 or (count == 2 and is_active(w-1, x-1, y-1, z-1, pocket_dim)):
                        next_cycle[z][y][x][w] = True


    return next_cycle

def day17_1():
    pocket_dim = [[[]]]
    pocket_dim[0][0] = [[char_to_bool(char) for char in line.strip()] for line in open("day17.txt")]

    print(pocket_dim)
    for i in range(6):
        pocket_dim = expand_dim(pocket_dim)
        print(i)

    print(total(pocket_dim))

def day17_2():
    pass


if __name__ == "__main__":
    day17_1()
    day17_2()