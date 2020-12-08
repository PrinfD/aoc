
def day1_1(): #788739
    res = set(int(line.strip()) for line in open("day1.txt"))
    print(set((n * (2020 - n)) for n in res if (2020 - n) in res))

def day1_2(): #222 843 955 178724430
    res = set(int(line.strip()) for line in open("day1.txt"))
    print([x * y * z for (x, y, z) in combinations(res, 3) if x + y + z == 2020])

def _day6_2_counter(group):
    return len({c for c in "abcdefghijklmnopqrstuvwxyz" if group.count(c) == 1 + group.count("\n")})