from sys import argv
from heapq import nlargest

def nLargest():
    fname = argv[1]
    linesIn = open(fname).readlines()
    d = {}
    n = int(linesIn[0])
    for line in linesIn[1:]:
        line = line.strip()
        d[len(line)] = line
    largest = nlargest(n, d.iteritems(), key=lambda x: x[0])
    for l in largest:
        print l[1]


if __name__ == '__main__':
    nLargest()
