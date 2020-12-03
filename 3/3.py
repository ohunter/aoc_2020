import os
from inspect import getsourcefile
from typing import List, Tuple

def slope_1_1(width: int, height: int) -> Tuple[int, int]:
    x, y = 0, 0

    while y < height:
        _x, _y = x, y
        x = (x+1) % width
        y += 1
        yield _x, _y

def slope_3_1(width: int, height: int) -> Tuple[int, int]:
    x, y = 0, 0

    while y < height:
        _x, _y = x, y
        x = (x+3) % width
        y += 1
        yield _x, _y

def slope_5_1(width: int, height: int) -> Tuple[int, int]:
    x, y = 0, 0

    while y < height:
        _x, _y = x, y
        x = (x+5) % width
        y += 1
        yield _x, _y

def slope_7_1(width: int, height: int) -> Tuple[int, int]:
    x, y = 0, 0

    while y < height:
        _x, _y = x, y
        x = (x+7) % width
        y += 1
        yield _x, _y

def slope_1_2(width: int, height: int) -> Tuple[int, int]:
    x, y = 0, 0

    while y < height:
        _x, _y = x, y
        x = (x+1) % width
        y += 2
        yield _x, _y

slopes = [
    slope_1_1,
    slope_3_1,
    slope_5_1,
    slope_7_1,
    slope_1_2,
]

def part_1(inp: List[str]):
    w = len(inp[0])
    h = len(inp)
    nt = 0

    for x, y in slope_3_1(w, h):
        if inp[y][x] == '#':
            nt += 1

    print (nt)

def part_2(inp: List[str]):
    w = len(inp[0])
    h = len(inp)
    v = 1

    for slope in slopes:
        k = 0
        for x, y in slope(w, h):
            if inp[y][x] == '#':
                k += 1
        
        v *= k

    print(v)

if __name__ == "__main__":
    l = None

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [x.replace('\n', '') for x in fi.readlines()]

    part_1(l)
    part_2(l)
