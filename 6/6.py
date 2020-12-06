import os
from inspect import getsourcefile
from typing import List

def part_1(inp: List[str]):
    print(sum([len({y for y in x if y != '\n'}) for x in inp]))

def part_2(inp: List[str]):
    tot = 0
    for grp in inp:
        indiv = [{y for y in x} for x in grp.split('\n')]
        total = indiv[0].union(*indiv)
        tot += len(total.intersection(*indiv))

    print(tot)

if __name__ == "__main__":
    l = []

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = fi.read(-1).split('\n\n')

    part_1(l)
    part_2(l)