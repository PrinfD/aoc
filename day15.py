import re

def day15(idx):
    nums = {}
    last_dif, cur_num, turn = 0, 0, 0
    honk_honk = [int(line) for line in open("day15.txt").readline().strip().split(",")]

    while turn < idx:
        cur_num = honk_honk[turn] if turn < len(honk_honk) else last_dif
        turn += 1
        last_dif = turn - nums.get(cur_num, turn)
        nums[cur_num] = turn

    print(cur_num)

if __name__ == "__main__":
    day15(2020)
    day15(30000000)