# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 9: Disk Fragmenter
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    return lines[0]

def expand(line):
    size = 0
    for c in line:
        size += int(c)
    disk = [-1] * size
    idx = 0
    id = 0
    isFile = True
    for c in line:
        count = int(c)
        for i in range(count):
            if isFile:
                disk[idx] = id
            idx += 1
        if isFile:
            id += 1
        isFile = not isFile
    return disk

def expand2(line):
    disk_map = []
    id = 0
    isFile = True
    for c in line:
        count = int(c)
        if isFile:
            disk_map.append((id, count))
            id += 1
        elif count != 0:
            disk_map.append((-1, count))
        isFile = not isFile
    return disk_map, id

def printDisk(disk):
    for num in disk:
        if num == -1:
            print('.', end="")
        else:
            print(num, end="")
    print()

def part1(data):
    """Solve part 1."""
    disk = expand(data)
    # printDisk(disk)
    left = 0
    right = len(disk) -1
    while left < right:
        if disk[left] != -1:
            left += 1
            continue
        if disk[right] == -1:
            right -= 1
            continue
        disk[left] = disk[right]
        disk[right] = -1
        left += 1
        right -= 1
    #printDisk(disk)
    result = 0
    for i in range(len(disk)):
        n = disk[i]
        if n == -1:
            break
        result += i * disk[i]
    return result

def part2Count(disk):
    result = 0
    pos = 0
    for fragment in disk:
        if fragment[0] == -1:
            pos += fragment[1]
            continue
        for i in range(fragment[1]):
            result += pos * fragment[0]
            pos += 1
    return result

def part2(data): # 6239712239037 is too low
    """Solve part 2."""
    disk, idx = expand2(data)
    while idx > 0:
        idx -= 1
        # make sure only move disk fragments to left, never right
        leftIdx = 0
        rightIdx = len(disk) -1
        fragment_size = 0
        fragment_right = disk[rightIdx]
        while rightIdx >= 0:
            fragment_right = disk[rightIdx]
            if fragment_right[0] == idx:
                fragment_size = fragment_right[1]
                break
            rightIdx -= 1

        fragment_left = disk[leftIdx]
        while leftIdx < rightIdx:
            fragment_left = disk[leftIdx]
            if fragment_left[0] == -1 and fragment_left[1] >= fragment_size:
                break
            leftIdx += 1
        if leftIdx >= rightIdx:
            continue
        # insert to left of leftIdx
        fragment_left = (fragment_left[0], fragment_left[1] - fragment_size)
        # need to combine the empty fragments
        fragment_right_new = (-1, fragment_right[1])
        disk.pop(rightIdx)
        disk.insert(rightIdx, fragment_right_new)
        while rightIdx > 0 and disk[rightIdx -1][0] == -1:
            rightIdx -= 1
        while (rightIdx + 1) < len(disk) and disk[rightIdx][0] == -1 and disk[rightIdx + 1][0] == -1:
            fragment_right_new = (-1, disk[rightIdx][1] + disk[rightIdx + 1][1])
            disk.pop(rightIdx + 1)
            disk.pop(rightIdx)
            disk.insert(rightIdx, fragment_right_new)
        disk.pop(leftIdx)
        if fragment_left[1] != 0: # don't insert if size 0
            disk.insert(leftIdx, fragment_left)
        disk.insert(leftIdx, fragment_right)
    return part2Count(disk)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    data2 = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data2)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
