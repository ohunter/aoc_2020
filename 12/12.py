import os
from inspect import getsourcefile
from typing import List, Tuple
from collections import defaultdict
import math

def part_1(inp: List[Tuple[str, int]]):
    card = defaultdict(int)
    card.update(
        {
            "E" : 0,
            "N" : 90,
            "W" : 180,
            "S" : 270,
        }
    )

    NS = 0
    EW = 0
    rot = 0

    for x in inp:
        print(NS, EW, rot)
        if x[0] == "L":
            rot = (rot + x[1]) % 360
        elif x[0] == "R":
            rot = (rot - x[1]) % 360
        else:
            _rot = rot if x[0] == "F" else card[x[0]]
            NS += x[1] * math.sin(math.radians(_rot))
            EW += x[1] * math.cos(math.radians(_rot))

    print(round(abs(NS) + abs(EW)))

def part_2(inp: List[Tuple[str, int]]):
    card = {
        "N": 0,
        "E": 1,
        "S": 2,
        "W": 3,
    }
    waypoint = [1, 10, 0, 0]

    NS = 0
    EW = 0

    for x in inp:
        if x[0] == "L":
            q = x[1] // 90
            waypoint = waypoint[q:] + waypoint[:q]
        elif x[0] == "R":
            q = x[1] // 90
            waypoint = waypoint[-q:] + waypoint[:-q]
        elif x[0] == "F":
            NS += x[1] * (waypoint[0] - waypoint[2])
            EW += x[1] * (waypoint[1] - waypoint[3])
        else:
            waypoint[card[x[0]]] += x[1]

    print(round(abs(NS) + abs(EW)))

if __name__ == "__main__":
    l = None

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [(x[0], int(x[1:])) for x in fi.readlines()]

    part_1(l)
    part_2(l)