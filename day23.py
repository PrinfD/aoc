import re
import numpy as np
import collections
import itertools

def read():
    return [line for line in open("day23.txt")]


class Element():
    __search = {}

    def __init__(self, val, next_element):
        self.val = val
        self.next = next_element

        Element.__search[val] = self

    @staticmethod
    def get(val):
        return Element.__search[val]

    def set_next(self, next_element):
        self.next = next_element

class Ring_List():
    def __init__(self, val):
        root = Element(val, None)
        root.set_next(root)
        self.head = root
        self.current = root
        self.tail = root

    def append(self, val):
        new_element = Element(val, self.head)
        self.tail.set_next(new_element)
        self.tail = new_element


def day23_1():
    order = [int(i) for i in read()[0]]
    cups = Ring_List(order[0])
    for i in order:
        if i != order[0]:
            cups.append(i)

    for x in range(100):
        cur_cup = cups.current
        extract = cur_cup.next
        to_connect = extract.next.next.next
        cur_cup.set_next(to_connect)

        next_label = cur_cup.val - 1
        if next_label < 1:
            next_label += len(order)

        while extract.val == next_label or extract.next.val == next_label or extract.next.next.val == next_label:
            next_label = next_label - 1
            if next_label < 1:
                next_label += len(order)

        insertion_point = Element.get(next_label)
        extract.next.next.set_next(insertion_point.next)
        insertion_point.next = extract
        cups.current = cups.current.next
    
    start = Element.get(1)
    string = str(start.val)
    el = start.next
    while el != start:
        string += str(el.val)
        el = el.next

    print(string)


def day23_2():
    order = [int(i) for i in read()[0]]
    for i in range(10, 1000000+1):
        order.append(i)
 
    cups = Ring_List(order[0])
    for i in order:
        if i != order[0]:
            cups.append(i)

    for x in range(10000000):
        cur_cup = cups.current
        extract = cur_cup.next
        to_connect = extract.next.next.next
        cur_cup.set_next(to_connect)

        next_label = cur_cup.val - 1
        if next_label < 1:
            next_label += len(order)

        while extract.val == next_label or extract.next.val == next_label or extract.next.next.val == next_label:
            next_label = next_label - 1
            if next_label < 1:
                next_label += len(order)

        insertion_point = Element.get(next_label)
        extract.next.next.set_next(insertion_point.next)
        insertion_point.next = extract

        cups.current = cups.current.next

        if x % 100000 == 0:
            print(x)
    
    el = Element.get(1)
    print(el.next.val, el.next.next.val, el.next.val * el.next.next.val)


if __name__ == "__main__":
    day23_1()
    day23_2()