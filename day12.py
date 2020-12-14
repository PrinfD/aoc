import re

def day12_1(): #-1423 -634 2057
    coms = [(line[:1], int(line[1:])) for line in open("day12.txt")]
    
    curDir = (-1, 0)
    curPos = [0, 0]

    for com, arg in coms:
        if com == "N":
            curPos[1] += arg
        elif com == "S":
            curPos[1] -= arg
        elif com == "W":
            curPos[0] += arg
        elif com == "E":
            curPos[0] -= arg
        elif com == "F":
            curPos[0] += arg * curDir[0]
            curPos[1] += arg * curDir[1]
        elif com == "L" or com == "R":
            r = (-arg // 90) % 4 if com == "L" else (arg // 90) % 4
            for i in range(0, r):
                curDir = (-curDir[1], curDir[0])
            
    
    print(curPos[0], curPos[1], abs(curPos[0]) + abs(curPos[1]))



def day12_2():
    coms = [(line[:1], int(line[1:])) for line in open("day12.txt")]
    
    cur = [-10, 1]
    ship = [0, 0]

    for com, arg in coms:
        if com == "N":
            cur[1] += arg
        elif com == "S":
            cur[1] -= arg
        elif com == "W":
            cur[0] += arg
        elif com == "E":
            cur[0] -= arg
        elif com == "F":
            ship[0] += cur[0] * arg
            ship[1] += cur[1] * arg
        elif com == "L" or com == "R":
            rotate = 0
            if com == "L":
                rotate = (-arg // 90) % 4
            else:
                rotate = (arg // 90) % 4
            for i in range(rotate):
                cur = [-cur[1], cur[0]]
    
    print(ship[0], ship[1], abs(ship[0]) + abs(ship[1]))

if __name__ == "__main__":
    day12_1()
    day12_2()