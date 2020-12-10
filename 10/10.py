import os
from inspect import getsourcefile
from typing import List
from collections import Counter, defaultdict

def part_1(inp: List[int]):
    inp.sort()
    cnt = Counter([y-x for x, y in zip(inp[:-1], inp[1:])])

    print(cnt[1] * cnt[3])

def part_2(inp: List[int]):
    solns = defaultdict(int)
    solns[inp[-1]] = 1

    for i in reversed(inp[:-1]):
        solns[i] = sum([solns[x] for x in range(i+1, i+4)])
    
    print(solns[0])

if __name__ == "__main__":
    l = []

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [0] + [int(x) for x in fi.readlines()]
        l.append(max(l)+3)

    part_1(l)
    part_2(l)