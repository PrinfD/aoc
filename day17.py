import re
import numpy as np


def in_range(v, r):
    return 0 <= v < r

def neig_count(x, y, z, pocket_dim):
    count = 0
    for dz in range(-1, 2):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if in_range(z + dz, len(pocket_dim)) and in_range(y + dy, len(pocket_dim[z+dz])) and in_range (x + dx, len(pocket_dim[z+dz][y+dy])):
                    if pocket_dim[z + dz][y + dy][x + dx]:
                        count += 1
    return count

def is_active(x, y, z, pocket_dim):
    return in_range(z, len(pocket_dim)) and in_range(y, len(pocket_dim[z])) and in_range(x, len(pocket_dim[z][y])) and pocket_dim[z][y][x]


def expand_dim(pocket_dim):
    next_cycle = np.zeros([len(pocket_dim)+2, len(pocket_dim[0])+2, len(pocket_dim[0][0])+2], dtype=bool)

    for z in range(len(next_cycle)):
        for y in range(len(next_cycle[z])):
            for x in range(len(next_cycle[z][y])):
                count = neig_count(x-1, y-1, z-1, pocket_dim)
                if count == 3 or (count == 4 and is_active(x-1, y-1, z-1, pocket_dim)):
                    next_cycle[z][y][x] = True

    return next_cycle

def day17_1():
    pocket_dim = [[[c == "#" for c in line.strip()] for line in open("day17.txt")]]

    print(pocket_dim)
    for i in range(6):
        print(i, np.sum(pocket_dim))
        pocket_dim = expand_dim(pocket_dim)

    print(np.sum(pocket_dim))


if __name__ == "__main__":
    day17_1()