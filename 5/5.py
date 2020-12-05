import os
from inspect import getsourcefile
from typing import Dict, List, Tuple
import re

def part_1(inp: List[Tuple[int, int]]):
    print(max([i * 8 + j for i, j in inp]))

def part_2(inp: List[Tuple[int, int]]):
    IDs = [i*8 + j for i, j in inp]
    IDs.sort()
    
    for i in IDs:
        if i+1 not in IDs:
            print(i+1)
            break

if __name__ == "__main__":
    l = []
    p = "(\w+):(\S+)"

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        for s in fi.readlines():
            tmp = s.translate(str.maketrans({'F':'0', 'L':'0', 'B':'1', 'R':'1'}))
            l.append((int(tmp[:7], 2), int(tmp[7:], 2)))

    part_1(l)
    part_2(l)