import re

def day10_construct():
    vals = [int(line) for line in open("day10.txt")]
    vals.append(0)
    vals.append(max(vals) + 3)
    return sorted(vals)

def day10_1(): #2210
    vals = day10_construct()
    difs = {1: 0, 3: 0}

    curVal = 0
    for val in vals:
        difs[val - curVal] = 1 + difs.get(val - curVal, 0)
        curVal = val

    print(difs[1] * difs[3])


def day10_2(): #7086739046912
    vals = day10_construct()
    valdict = {key:0 for key in vals}
    valdict[0] = 1

    for val in vals:
        for reachable in range(val + 1, val + 4):
            if valdict.get(reachable) != None:
                valdict[reachable] += valdict[val]

    print(valdict[max(vals)])

if __name__ == "__main__":
    day10_1()
    day10_2()
