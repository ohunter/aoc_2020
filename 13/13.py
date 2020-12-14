import os
from inspect import getsourcefile
from typing import List
import math
import numpy as np

def part_1(tm: int, routes: List[int]):
    tmp = [x for x in routes if isinstance(x, int)]
    nxt = [math.ceil(tm / x) * x for x in tmp]
    i = nxt.index(min(nxt))

    print ((nxt[i] - tm) * tmp[i])


def part_2(routes: List[int]):
    nums = [x for x in routes if isinstance(x, int)]
    steps = [i for i, x in enumerate(routes) if x != 'x']

    k = 0
    inc = [np.lcm.reduce(nums[:i+1]) for i in range(len(nums)-1)]
    
    for i in range(1, len(nums)):
        x = inc.pop(0)
        while not all([k%a == (a-steps[b])%a for b,a in enumerate(nums[:i+1])]):
            k += x

    print(k)


if __name__ == "__main__":
    t = 0
    l = []

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        t = int(fi.readline())
        l = [int(x) if x != 'x' else x for x in fi.readline().split(',')]

    part_1(t, l)
    part_2(l)