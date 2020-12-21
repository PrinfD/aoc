import re
import numpy as np
import itertools


def in_range(v, r):
    return 0 <= v < len(r)


def is_active(w, x, y, z, pocket_dim):
    return in_range(z, pocket_dim) and in_range(y, pocket_dim[z]) and in_range(x, pocket_dim[z,y]) and in_range(w, pocket_dim[z,y,x]) and pocket_dim[z,y,x,w]


def neig_count(w, x, y, z, pocket_dim):
    count = 0
    for dz, dy, dx, dw in itertools.product(range(-1, 2), repeat=pocket_dim.ndim):
        if is_active(w+dw, x+dx, y+dy, z+dz, pocket_dim):
            count += 1
    return count


def expand_dim(pocket_dim):
    size = np.array(pocket_dim.shape) + 2
    next_cycle = np.empty(size, dtype=bool)

    nz, ny, nx, nw = size
    for z, y, x, w in itertools.product(range(nz), range(ny), range(nx), range(nw)):
        count = neig_count(w-1, x-1, y-1, z-1, pocket_dim)
        next_cycle[z,y,x,w] = count == 3 or (count == 4 and is_active(w-1, x-1, y-1, z-1, pocket_dim))

    return next_cycle


def day17_2():
    pocket_dim = np.array([[[[char == "#" for char in line.strip()] for line in open("day17.txt")]]], dtype=bool)

    for i in range(6):
        print(i, np.sum(pocket_dim))
        pocket_dim = expand_dim(pocket_dim)

    print(np.sum(pocket_dim))


if __name__ == "__main__":
    day17_2()
