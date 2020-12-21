import re
import numpy as np
import collections


def read():
    return [line for line in open("day21.txt")]


def get_foods_by_allergen():
    foods_by_allergen = {}

    for line in read():
        foods_string, allergene_string = line.strip().split(" (")
        foods = set(foods_string.split(" "))

        for allergene in set(allergene_string[9:-1].split(", ")):
            if allergene in foods_by_allergen:
                foods_by_allergen[allergene].intersection_update(foods)
            else:
                foods_by_allergen[allergene] = set() | foods

    while any(len(food) != 1 for food in foods_by_allergen.values()):
        for allergen, foods in foods_by_allergen.items():
            if len(foods) == 1:
               for other_allergene, other_foods in foods_by_allergen.items():
                    if other_allergene != allergen:
                        other_foods -= foods
 
    return {key:val.pop() for key, val in foods_by_allergen.items()}


def day21_1():
    foods_by_allergen = get_foods_by_allergen()
    ls = []
    for line in read():
        ls += line.strip().split(" (")[0].split(" ")

    count = len([food for food in ls if food not in foods_by_allergen.values()])
    print(count)


def day21_2():
    foods_by_allergen = get_foods_by_allergen()
    dangerous_list = ",".join(foods_by_allergen[key] for key in sorted(foods_by_allergen.keys()))
    print(foods_by_allergen)
    print(dangerous_list)


if __name__ == "__main__":
    day21_1()
    day21_2()