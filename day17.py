import re
import numpy as np
import itertools


def in_range(v, r):
    return 0 <= v < len(r)


def is_active(x, y, z, pocket_dim):
    return in_range(z, pocket_dim) and in_range(y, pocket_dim[z]) and in_range(x, pocket_dim[z,y]) and pocket_dim[z,y,x]


def neig_count(x, y, z, pocket_dim):
    count = 0
    for dz, dy, dx in itertools.product(range(-1, 2), repeat=3):
        if is_active(x+dx, y+dy, z+dz, pocket_dim):
            count += 1
    return count


def expand_dim(pocket_dim):
    size = np.add(np.array(pocket_dim.shape), 2)
    next_cycle = np.empty(size, dtype=bool)

    nz, ny, nx = size
    for z, y, x in itertools.product(range(nz), range(ny), range(nx)):
        count = neig_count(x-1, y-1, z-1, pocket_dim)
        next_cycle[z,y,x] = count == 3 or (count == 4 and is_active(x-1, y-1, z-1, pocket_dim))

    return next_cycle

def day17_1():
    pocket_dim = np.array([[[c == "#" for c in line.strip()] for line in open("day17.txt")]], dtype=bool)
    for i in range(6):
        print(i, np.sum(pocket_dim))
        pocket_dim = expand_dim(pocket_dim)

    print(np.sum(pocket_dim))


if __name__ == "__main__":
    day17_1()