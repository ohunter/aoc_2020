import os
from inspect import getsourcefile
from typing import Dict, List

def nested_sum(key: str, inp: Dict[str, int]):
    if key not in inp:
        return 0
    else:
        return 1 + sum([v * nested_sum(k, inp) for k, v in inp[key].items()])

def part_1(inp: List[List[str]]):
    ratios = {}

    for x in inp:
        i = len(x)
        key = f"{x[0]} {x[1]}"
        if i == 3:
            ratios[key] = {"" : 0}
        elif i >= 5:
            ratios[key] = {f"{x[a+1]} {x[a+2]}" : int(x[a]) for a in range(2, len(x), 3)}

    n1 = {k for k, v in ratios.items() if "shiny gold" in v.keys()}
    n2 = {}

    while n1.difference(n2):
        n2 = n1
        n1 = {k for k, v in ratios.items() if any([m for m in v.keys() if m in n2])}.union(n2)

    print(len(n1))

def part_2(inp: List):
    ratios = {}

    for x in inp:
        i = len(x)
        key = f"{x[0]} {x[1]}"
        if i == 3:
            ratios[key] = {"" : 0}
        elif i >= 5:
            ratios[key] = {f"{x[a+1]} {x[a+2]}" : int(x[a]) for a in range(2, len(x), 3)}

    print(nested_sum("shiny gold", ratios)-1)

if __name__ == "__main__":
    l = []
    filler = ["bags", ",", "contain", "bag", "other", "bags.", "bag,", "bag.", "bags,"]

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [[word if word != "no" else "0" for word in line.strip().split(' ') if word not in filler] for line in fi.readlines()]

    part_1(l)
    part_2(l)