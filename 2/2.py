import os
from inspect import getsourcefile
from typing import List, Tuple
import re

def part_1(inp: List[Tuple[int, int, str, str]]):
    count = 0

    for small, large, needle, haystack in inp:
        if small <= haystack.count(needle) <= large:
            count += 1

    print(count)

def part_2(inp: List[Tuple[int, int, str, str]]):
    count = 0

    for i, j, needle, haystack in inp:
        if haystack[i-1:].startswith(needle) ^ haystack[j-1:].startswith(needle):
            count += 1

    print(count)

if __name__ == "__main__":
    l = None
    p = '(\d+)-(\d+) (\w): (\w+)'

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [(int(a), int(b), c, d) for a, b, c, d in re.findall(p, fi.read(-1))]

    part_1(l)
    part_2(l)
