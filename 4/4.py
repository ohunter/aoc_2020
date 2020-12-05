import os
from inspect import getsourcefile
from typing import Dict, List
import re

def part_1(inp: List[Dict[str, int]]):
    num = 0

    for ID in inp:
        if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.difference(ID.keys()) <= {'cid'}:
            num += 1

    print(num)

def part_2(inp: List[Dict[str, int]]):
    num = 0

    for ID in inp:
        if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.difference(ID.keys()) <= {'cid'}:
            valid = True
            for k, v in ID.items():
                if not valid:
                    break
                if k == 'byr':
                    valid &= len(v) == 4 and 1920 <= int(v) <= 2002
                elif k == 'iyr':
                    valid &= len(v) == 4 and 2010 <= int(v) <= 2020
                elif k == 'eyr':
                    valid &= len(v) == 4 and 2020 <= int(v) <= 2030
                elif k == 'hgt':
                    valid &= (v.endswith('cm') and 150 <= int(v[:-2]) <= 193) or (v.endswith('in') and 59 <= int(v[:-2]) <= 76)
                elif k == 'hcl':
                    valid &= len(v) == 7 and re.search('\#[0-9a-f]{6}', v)
                elif k == 'ecl':
                    valid &= v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                elif k == 'pid':
                    valid &= len(v) == 9 and re.search('[0-9]{9}', v)

            if valid:
                num += 1

    print(num)

if __name__ == "__main__":
    l = None
    p = "(\w+):(\S+)"

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = [{k:v for k, v in re.findall(p, ID)} for ID in fi.read(-1).split('\n\n')]

    part_1(l)
    part_2(l)