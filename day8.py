import re

def _execute(lines):
    lines_executed = set()
    acc = 0
    line = 0

    while line < len(lines) and line not in lines_executed:
        lines_executed.add(line)

        operator, operand = lines[line].split()
        operand = int(operand)

        if operator == "acc":
            acc += operand
        elif operator == "jmp":
            line += operand - 1
        
        line += 1

    return (line == len(lines), line, acc)

def day8_1():
    print(_execute(open("day8.txt").readlines()))

def day8_2(): #1358
    lines = open("day8.txt").readlines()
    mapped_op = {"jmp": "nop", "nop": "jmp"}

    for idx, line in enumerate(lines):
        op, opd = line.split()
        lines[idx] = mapped_op.get(op, op) + " " + opd
        result = _execute(lines)
        if result[0]:
            print("Ok", idx, result)

        lines[idx] = line

if __name__ == "__main__":
    day8_1()
    day8_2()