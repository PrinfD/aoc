
import re
import itertools

def count_seats(x, y, seats):
    count = 0

    for xi in range(x - 1, x + 2):
        for yi in range(y - 1, y + 2):
            if (xi != x or yi != y) and \
                    xi >= 0 and xi < len(seats[y - 1]) and \
                    yi >= 0 and yi < len(seats):
                if seats[yi][xi] == 2:
                    count += 1

    return count


def day11(seats):
    noo_seats = [[x for x in row] for row in seats]
    changed = False

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            seat = seats[y][x]
            if seat == 1:
                if count_seats(x, y, seats) == 0:
                    noo_seats[y][x] = 2
                    changed = True
            elif seat == 2:
                if count_seats(x, y, seats) >= 4:
                    noo_seats[y][x] = 1
                    changed = True
    
    if changed:
        return noo_seats

    return None

def mod_char(char):
    if char == "L":
        return 1
    else:
        return 0

def count_occupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 2:
                count += 1
    return count

def day11_1():
    seats = [[mod_char(char) for char in line.strip()] for line in open("day11.txt")]

    prev = seats
    while seats != None:
        prev = seats
        seats = day11(seats)

    print(count_occupied(prev))


def count_seats23(x, y, dx, dy, seats):
    x = x + dx
    y = y + dy

    while y >= 0 and y < len(seats) and x >= 0 and x < len(seats[y]):
        if seats[y][x] == 2:
            return 1
        elif seats[y][x] == 1:
            return 0

        x = x + dx
        y = y + dy

    return 0

def count_seats2(x, y, seats):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                count += count_seats23(x, y, dx, dy, seats)
    return count


def day112(seats):
    noo_seats = [[x for x in row] for row in seats]
    changed = False

    for y in range(len(seats)):
        for x in range(len(seats[y])):
            seat = seats[y][x]
            if seat == 1:
                if count_seats2(x, y, seats) == 0:
                    noo_seats[y][x] = 2
                    changed = True
            elif seat == 2:
                if count_seats2(x, y, seats) >= 5:
                    noo_seats[y][x] = 1
                    changed = True
    
    if changed:
        return noo_seats

    return None

def day11_2():
    seats = [[mod_char(char) for char in line.strip()] for line in open("day11.txt")]

    prev = seats
    while seats != None:
        prev = seats
        seats = day112(seats)

    print(count_occupied(prev))


if __name__ == "__main__":
    for c in itertools.permutations((1, 0, -1), 2):
        print(c)

    day11_1()
    day11_2()