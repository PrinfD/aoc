import re
import collections
import numpy as np

def eval_polish(stack):
    deq = collections.deque(stack)
    working_stack = []

    while deq:
        expr = deq.popleft()
        if expr.isnumeric():
            working_stack.append(int(expr))
        else:
            l, r = working_stack.pop(), working_stack.pop()
            if expr == "*":
                working_stack.append(l * r)
            elif expr == "+":
                working_stack.append(l + r)
    
    return working_stack[0]

def evalualte(expr, precedence):
    op_stack = []
    result = []

    for c in expr:
        if c.isnumeric():
            result.append(c)
        elif c == "+" or c == "*":
            while op_stack and precedence[c] <= precedence[op_stack[-1]]:
                result.append(op_stack.pop())
  
            op_stack.append(c)
        elif c == "(":
            op_stack.append(c)
        elif c == ")":
            cur = op_stack.pop()
            while cur != "(":
                result.append(cur)
                cur = op_stack.pop()

    result += reversed(op_stack)
    return eval_polish(result)

def eval(expr):
    return evalualte(expr, {"+": 1, "*": 1, "(": -9999})

def advanced_eval(expr):
    return evalualte(expr, {"+": 2, "*": 1, "(": -9999})

def day18_1():
    print(sum([eval(line.strip()) for line in open("day18.txt")]))

def day18_2():
    print(sum([advanced_eval(line.strip()) for line in open("day18.txt")]))


if __name__ == "__main__":
    day18_1()   #3348222486398
    day18_2()   #43423343619505
