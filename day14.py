import re
import numpy as np


def day14_1():
    mem = {}
    mask1 = 0
    mask0 = 0

    f = open("day14.txt")
    for line in f:
        com, val = line.strip().split(" = ")
        if com == "mask":
            mask1 = int(val.replace("X", "0"), base=2)
            mask0 = int(val.replace("X", "1"), base=2)
        else:
            val = int(val)
            idx = int(com[4:-1])
            mem[idx] = (val | mask1) & mask0

    f.close()
    print(sum(mem.values()))

def gen_idxs(mask):
    idxs = []
    for i in range(2 ** mask.count("X")):
        m = {0: list(mask), 1: list(mask)}
        
        for idx, str_idx in enumerate([m.start() for m in re.finditer('X', mask)]):
            bit = (i >> idx) & 1
            m[bit][str_idx] = str(bit)

        mi0 = int("".join(m[0]).replace("X", "1").replace("N", "1"), base=2)
        mi1 = int("".join(m[1]).replace("X", "0").replace("N", "0"), base=2)
        idxs.append((mi0, mi1))
    return idxs

def day14_2():
    mem = {}
    mask1 = 0
    maskX = 0

    f = open("day14.txt")
    for line in f:
        com, val = line.strip().split(" = ")
        if com == "mask":
            mask1 = int(val.replace("X", "0"), base=2)
            maskX = val.replace("1", "0").replace("0", "N")
        else:
            idx = int(com[4:-1]) | mask1
            for m0, m1 in gen_idxs(maskX):
                mem[(idx | m1) & m0] = int(val)

    f.close()
    print(sum(mem.values()))

if __name__ == "__main__":
    day14_1()
    day14_2()