import re
import numpy as np
import collections


def get_decks():
    f = "".join([line for line in open("day22.txt")])
    sp1, sp2 = f.strip().split("\n\n")

    p1 = collections.deque([int(n) for n in sp1.splitlines()[1:]])
    p2 = collections.deque([int(n) for n in sp2.splitlines()[1:]])

    return (p1, p2)

def calc_score(deck):
    return sum(deck[-i] * i for i in range(1 + len(deck)))

def determine_game_result(p1, p2):
    if p1:
        print("Player 1 wins!", "Score: ", calc_score(p1))
    else:
        print("Player 2 wins!", "Score: ", calc_score(p2))


def play_simple_game(p1, p2):
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))
    
    return len(p1) > 0


def play_recursive_game(p1, p2, print_game):
    round = 0
    o = set()
    while p1 and p2:
        round += 1

        if not add_ordering(p1, p2, o):
            break

        c1, c2 = p1.popleft(), p2.popleft()

        if print_game:
            print("-------- Round", round, " -------------")
            print("Player 1 deck:", p1)
            print("Player 2 deck:", p2)
            print("Player 1 card:" , c1)
            print("Player 2 card:" , c2)
            print()

        if get_winner_of_round(p1, p2, c1, c2):
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))

    return len(p1) > 0

def get_winner_of_round(p1, p2, c1, c2): #true if p1 wins, false if p2 wins
    if c1 <= len(p1) and c2 <= len(p2):
        p1copy = collections.deque([p1[i] for i in range(c1)])
        p2copy = collections.deque([p2[i] for i in range(c2)])
        return play_recursive_game(p1copy, p2copy, False)
    else:
        return c1 > c2

def add_ordering(p1, p2, o):
    po = "".join([str(i) for i in p1]) + "x" + "".join([str(i) for i in p2])
    if po in o:
        return False

    o.add(po)
    return True


def day22_1(): #30780
    p1, p2 = get_decks()
    play_simple_game(p1, p2)
    determine_game_result(p1, p2)

def day22_2(): #36621
    p1, p2 = get_decks()
    play_recursive_game(p1, p2, True)
    determine_game_result(p1, p2)


if __name__ == "__main__":
    day22_1()
    day22_2()