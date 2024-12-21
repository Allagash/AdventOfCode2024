# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 5: Print Queue
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    dict = defaultdict(set)
    nums = []
    for l in lines:
        if '|' in l:
            vals = l.split('|')
            dict[int(vals[0])].add(int(vals[1]))
        else:
            vals = l.split(',')
            if len(vals) > 0 and len(vals[0]) > 0:
                nums.append([int(item) for item in vals])
    return (dict, nums)

def correctOrder(nums, dict):
    # inefficient
    for i in range(len(nums)):
        num = nums[i]
        for j in range(i + 1, len(nums)):
            next = nums[j]
            if num in dict[next]:
                return False
    return True

def part1(data):
    """Solve part 1."""
    result = 0
    dict, nums = data
    for l in nums:
        if correctOrder(l, dict):
            idx = len(l) // 2
            #print("correct: ", l, " index is ", idx, " val is ", l[idx] )
            result += l[idx]
    return result

def sortRank(item1, item2, dict):
    if item2 in dict[item1]:
        return -1
    elif item1 in dict[item2]:
        return 1
    else:
        return 0

def part2(data): # 10207 is too high
    """Solve part 2."""
    result = 0
    dict, nums = data
    """
    keys = list(dict.keys())
    for k in keys:
        entries = dict[k].copy()
        already_done = set()
        while entries: # not null
            entry = entries.pop()
            if entry in already_done:
                continue
            else:
                already_done.add(entry)
            additional = dict[entry]
            entries.update(additional)
            dict[k].update(additional)
    """
    # print(dict)

    for l in nums:
        idx = len(l) // 2
        if not correctOrder(l, dict):
            good_list = sorted(l, key=cmp_to_key(lambda item1, item2: sortRank(item1, item2, dict)))
            result += good_list[idx]

    return result

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
