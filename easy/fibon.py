import sys
import math


def nthFibo():
    fname = sys.argv[1]
    numList = map(lambda x: int(x.strip()), open(fname).readlines())
    phi = (1 + math.sqrt(5)) / 2
    for num in numList:
        fibo = round((phi ** num) / math.sqrt(5))
        print int(fibo)

if __name__ == "__main__":
    nthFibo()