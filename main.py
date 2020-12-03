import re
import numpy as np
import math

def day1_1():
    res = set(int(line.strip()) for line in open("day1.txt"))
    print(set((n * (2020 - n)) for n in res if (2020 - n) in res))

def day1_2(): #222 843 955 178724430
    res = set(int(line.strip()) for line in open("day1.txt"))

    for val1 in res:
        for val2 in res:
            if val1 != val2 and (2020 - val1 - val2) in res:
                print(val1, val2, 2020 - val1 - val2, val1*val2* (2020 - val1 - val2))


def _day2_1_check(r):
    return int(r.group(1)) <= r.group(4).count(r.group(3)) <= int(r.group(2))

def _day2_2_check(r):
    return (r.group(4)[int(r.group(1))- 1] == r.group(3)) ^ (r.group(4)[int(r.group(2)) - 1] == r.group(3))

def _day2(method):
    print(sum(1 for line in open("day2.tx") if method(re.match(r"(\d+)\-(\d+) (\w): (\w*)", line.strip()))))

def day2_1():
    _day2(_day2_1_check)

def day2_2():
    _day2(_day2_2_check)

def _day3(x, y):
    tree_map = [line.strip() for line in open("day3.txt")]
    return sum(1 for i in range(0, math.ceil(len(tree_map) / y)) if tree_map[i * y][(i * x) % len(tree_map[i])] == "#")

def day3_1(): #173
    print(_day3(3, 1))

def day3_2(): #4385176320
    print(np.product([_day3(i % 8, 1 + i // 9) for i in range(1, 10, 2)], dtype=np.uint64))


if __name__ == "__main__":
    day3_2()
