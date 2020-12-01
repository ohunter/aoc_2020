import os
from importlib.machinery import SourceFileLoader
from inspect import getsourcefile

if __name__ == "__main__":
    l = None

    with open(f"{os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))}/input", 'r') as fi:
        l = set([int(x) for x in fi.readlines()])

    for i in l:
        n = 2020 - i

        if n in l:
            print(i*n)
            break