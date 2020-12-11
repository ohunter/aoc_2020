import os
from inspect import getsourcefile
from typing import List, Tuple
from copy import deepcopy

def dist(p1: Tuple[int, int], p2: Tuple[int, int]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part_1(inp: List[List[chr]]):
    change = True
    b2 = deepcopy(inp)

    while change:
        b1 = deepcopy(b2)
        for i, j in [(x, y) for x in range(len(inp)) for y in range(len(inp[0]))]:
            if inp[i][j] == ".":
                continue
            else:
                idx = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) if 0 <= x < len(inp) and 0 <= y < len(inp[0]) and (x, y) != (i, j)]
                
                if b1[i][j] == "L" and not any([True if b1[a][b] == "#" else False for a, b in idx]):
                    b2[i][j] = "#"
                elif b1[i][j] == "#" and sum([True if b1[a][b] == "#" else False for a, b in idx]) >= 4:
                    b2[i][j] = "L"
        change = b1 != b2

    print(sum([True for x in b2 for y in x if y == "#"]))

def part_2(inp: List[List[chr]]):
    change = True
    b2 = deepcopy(inp)

    while change:
        b1 = deepcopy(b2)
        for i, j in [(x, y) for x in range(len(inp)) for y in range(len(inp[0]))]:
            if inp[i][j] == ".":
                continue
            else:
                idx = [x[0] for x in [
                    [(i, y) for y in range(j, -1, -1) if (i, j) != (i, y) and inp[i][y] != "."],
                    [(i, y) for y in range(j+1, len(inp[0])) if (i, j) != (i, y) and inp[i][y] != "."],
                    [(x, j) for x in range(i, -1, -1) if (i, j) != (x, j) and inp[x][j] != "."],
                    [(x, j) for x in range(i+1, len(inp)) if (i, j) != (x, j) and inp[x][j] != "."],
                    [(x, y) for x, y in zip(range(i-1, -1, -1), range(j-1, -1, -1)) if inp[x][y] != "."], # towards 0,0
                    [(x, y) for x, y in zip(range(i-1, -1, -1), range(j+1, len(inp[0]))) if inp[x][y] != "."], # towards 0,m
                    [(x, y) for x, y in zip(range(i+1, len(inp)), range(j-1, -1, -1)) if inp[x][y] != "."], # towards n,0
                    [(x, y) for x, y in zip(range(i+1, len(inp)), range(j+1, len(inp[0]))) if inp[x][y] != "."], # towards n,m
                ] if x]

                if b1[i][j] == "L" and not any([True if b1[a][b] == "#" else False for a, b in idx]):
                    b2[i][j] = "#"
                elif b1[i][j] == "#" and sum([True if b1[a][b] == "#" else False for a, b in idx]) >= 5:
                    b2[i][j] = "L"
        
        change = b1 != b2

    print(sum([True for x in b2 for y in x if y == "#"]))

if __name__ == "__main__":
    l = None

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [[x for x in line.strip()] for line in fi.readlines()]

    part_1(l)
    part_2(l)