import re

def day15(idx):
    nums = {}
    last_dif = 0
    cur_num = 0
    turn = 0
    
    for line in open("day15.txt").readline().strip().split(","):
        turn += 1
        cur_num = int(line)
        last_dif = turn - nums.get(cur_num, turn)
        nums[cur_num] = turn

    while turn < idx:
        turn += 1
        cur_num = last_dif
        last_dif = turn - nums.get(cur_num, turn)
        nums[cur_num] = turn

    print(cur_num)

if __name__ == "__main__":
    day15(2020)
    day15(30000000)