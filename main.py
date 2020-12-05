import re
import numpy as np
import math

def _count(iterable, condition):
    return len([i for i in iterable if condition(i)])

def day1_1(): #788739
    res = set(int(line.strip()) for line in open("day1.txt"))
    print(set((n * (2020 - n)) for n in res if (2020 - n) in res))

def day1_2(): #222 843 955 178724430
    res = set(int(line.strip()) for line in open("day1.txt"))

    for val1 in res:
        for val2 in res:
            if val1 < val2 and (2020 - val1 - val2) in res:
                print(val1, val2, 2020 - val1 - val2, val1*val2* (2020 - val1 - val2))


def _day2_1_check(r):
    return int(r.group(1)) <= r.group(4).count(r.group(3)) <= int(r.group(2))

def _day2_2_check(r):
    return (r.group(4)[int(r.group(1))- 1] == r.group(3)) ^ (r.group(4)[int(r.group(2)) - 1] == r.group(3))

def _day2(method):
    print(_count(open("day2.txt"), lambda line: method(re.match(r"(\d+)\-(\d+) (\w): (\w*)", line.strip()))))

def day2_1(): #383
    _day2(_day2_1_check)

def day2_2(): #272
    _day2(_day2_2_check)

def _day3(x, y):
    tree_map = [line.strip() for line in open("day3.txt")]
    return sum(1 for i in range(0, math.ceil(len(tree_map) / y)) if tree_map[i * y][(i * x) % len(tree_map[i])] == "#")

def day3_1(): #173
    print(_day3(3, 1))

def day3_2(): #4385176320
    print(np.product([_day3(i % 8, 1 + i // 9) for i in range(1, 10, 2)], dtype=np.uint64))

def _day4_filtered():
    result = "".join(open("day4.txt").readlines()) #Manually removed last linebreak
    ports = [re.split(r"\s", row) for row in result.split("\n\n")]
    ports = [dict(field.split(":") for field in port) for port in ports]
    expected = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return [port for port in ports if expected.issubset(port.keys())]

def day4_1(): #242
    print(len(_day4_filtered()))

def _check_str_num(str, lowerbound, upperbound):
    return str.isnumeric() and lowerbound <= int(str) <= upperbound

def _day4_2_check(port):
    valid = _check_str_num(port["byr"], 1920, 2002)
    valid &= _check_str_num(port["iyr"], 2010, 2020)
    valid &= _check_str_num(port["eyr"], 2020, 2030)
    valid &= (port["hgt"][-2:] == "in" and _check_str_num(port["hgt"][:-2], 59, 76)) or (port["hgt"][-2:] == "cm" and _check_str_num(port["hgt"][:-2], 150, 193))
    valid &= bool(re.match(r"^#[0-9a-zA-Z]{6}$", port["hcl"]))
    valid &= port["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid &= bool(re.match(r"^\d{9}$", port["pid"]))
    return valid

def day4_2(): #186
    print(_count(_day4_filtered(), _day4_2_check))

def _day5(seat):
    row = seat[:7].replace("F", "0").replace("B", "1")
    column = seat[-4:].replace("L", "0").replace("R", "1")
    return int(row, base=2) * 8 + int(column, base=2)

def _day5_ids():
    return {_day5(seat) for seat in open("day5.txt")}

def day5_1(): #828
    print(max(_day5_ids()))

def day5_2(): #556
    ids = _day5_ids()
    print(set(range(min(ids), max(ids))).difference(ids))

if __name__ == "__main__":
    day1_1()
    day1_2()
    day2_1()
    day2_2()
    day3_1()
    day3_2()
    day4_1()
    day4_2()
