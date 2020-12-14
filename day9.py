import re
from itertools import combinations

def day9_1_get():
    depth = 25
    nums = [int(line) for line in open("day9.txt")]
    
    for i in range(depth, len(nums)):
        combs = combinations(nums[i - depth:i], 2) 
        if all(x + y != nums[i] for x, y in combs):
            return nums[i]

def day9_1(): #70639851
    print(day9_1_get())

def day9_2():
    todo = day9_1_get()
    nums = [int(line) for line in open("day9.txt")]
    found = False

    for i in range(0, len(nums)):
        for n in range(i + 2, len(nums)):
            total = sum(nums[i:n])
            if total == todo:
                print(min(nums[i:n]) + max(nums[i:n]), nums[i:n])
                found = True
                break
            elif total > todo:
                break

        if found:
            break

def day9_2():
    todo = day9_1_get()
    nums = [int(line) for line in open("day9.txt")]

    lpr = 0
    rpr = 1

    while rpr <= len(nums):
        total = sum(nums[lpr:rpr])
        if total == todo:
            print(min(nums[lpr:rpr]) + max(nums[lpr:rpr]), nums[lpr:rpr])
            break
        elif total < todo:
            rpr += 1
        elif total > todo:
            lpr += 1

if __name__ == "__main__":
    day9_1()
    day9_2()