import re
import numpy as np

def day13_1():
    f = open("day13.txt")
    time = int(f.readline().strip())
    ids = [int(x) for x in f.readline().strip().split(",") if x != "x"]
    
    xs = {(x - (time % x), x) for x in ids}
    print(xs)
    print(min(xs))
    print(6 * 383)

def day13_2():
    f = open("day13.txt")
    time = int(f.readline().strip())
    ids = {x:int(y) for x, y in enumerate(f.readline().strip().split(",")) if y != "x"}
    print(ids)

    minis, id = ids.popitem()
    x = (-minis) % id
    ns = id
    print(x, ns)

    for mins, id in ids.items():
        print(id, mins)
        actual_remainder = (-mins) % id
        mult = 0
        while True:
            if (x + (mult * ns)) % id == actual_remainder:
                x = x + (mult * ns)
                ns = ns * id
                print("x: ", x)
                break
            mult += 1


if __name__ == "__main__":
    #day13_1()
    day13_2()