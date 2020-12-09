import os
from inspect import getsourcefile
from typing import List, Tuple
from copy import deepcopy

def part_1(inp: List[int], _min):
    offset = _min

    while offset < len(inp):
        k = inp[offset]

        for i in inp[offset-_min:offset]:
            if k-i in inp[offset-_min:offset]:
                break
        else:
            print(k)
            break
        
        offset += 1

def part_2(inp: List[int], _min):
    offset = _min
    val = 0

    while offset < len(inp):
        k = inp[offset]

        for i in inp[offset-_min:offset]:
            if k-i in inp[offset-_min:offset]:
                break
        else:
            val = k
            break
        
        offset += 1

    o1 = 0
    o2 = 1

    while sum(inp[o1:o2]) != val:
        if sum(inp[o1:o2]) < val:
            o2 += 1
        elif sum(inp[o1:o2]) > val:
            o1 += 1
            o2 = o1 + 1

    print(min(inp[o1:o2]) + max(inp[o1:o2]))

if __name__ == "__main__":
    l = []

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [int(x) for x in fi.readlines()]

    part_1(l, 25)
    part_2(l, 25)