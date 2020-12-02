import os
from inspect import getsourcefile
from typing import List

def part_1(inp: List[int]):

    inp.sort()

    for i in inp:
        n = 2020 - i

        if n in inp:
            print(i*n)
            return

def part_2(inp: List[int]):

    inp.sort()

    for i, x in enumerate(inp):
        for j, y in enumerate(inp[i:], i):
            for z in inp[j:]:
                if x + y + z == 2020:
                    print (x*y*z)
                    return

if __name__ == "__main__":
    l = None

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [int(x) for x in fi.readlines()]

    part_1(l)
    part_2(l)
