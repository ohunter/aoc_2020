import os
from inspect import getsourcefile
from typing import List, Tuple
from copy import deepcopy

def part_1(inp: List[Tuple[str, int]]):
    acc = 0
    pc = 0
    visited = []
    
    while pc not in visited:
        visited.append(pc)

        step = 1

        if inp[pc][0] == "acc":
            acc += inp[pc][1]
        elif inp[pc][0] == "jmp":
            step = inp[pc][1]

        pc += step
        
    print(acc)

def part_2(inp: List[Tuple[str, int]]):
    branch_stack = [
        {
            "pc" : 0,
            "acc" : 0,
            "visited" : [],
            "instr" : inp,
            "altered" : False
        }

    ]
        
    while branch_stack:
        b = branch_stack.pop()

        while b["pc"] < len(inp) and b["pc"] not in b["visited"]:
            b["visited"].append(b["pc"])
            step = 1

            if b["instr"][b["pc"]][0] == "acc":
                b["acc"] += b["instr"][b["pc"]][1]
            elif b["instr"][b["pc"]][0] == "nop":
                if not b["altered"]:
                    tmp = deepcopy(b)

                    tmp["instr"][tmp["pc"]][0] = "jmp"
                    tmp["pc"] += tmp["instr"][tmp["pc"]][1]
                    tmp["altered"] = True

                    branch_stack.append(tmp)
            elif b["instr"][b["pc"]][0] == "jmp":
                if not b["altered"]:
                    tmp = deepcopy(b)

                    tmp["instr"][tmp["pc"]][0] = "nop"
                    tmp["pc"] += 1
                    tmp["altered"] = True

                    branch_stack.append(tmp)

                step = b["instr"][b["pc"]][1]

            b["pc"] += step

        if b["pc"] >= len(inp):
            print(b["acc"])
            break


if __name__ == "__main__":
    l = []

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [(instr.split()[0], int(instr.split()[1])) for instr in fi.readlines()]

    part_1([[a for a in b] for b in l])
    part_2([[a for a in b] for b in l])