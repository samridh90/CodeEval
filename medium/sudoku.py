from sys import argv
from collections import Counter


def isValidSudoku(l, n):
    c = Counter(l)
    for i in xrange(1, n+1):
        if c[i] != n:
            return False
    return True


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        n, l = ip.strip().split(";")
        n = int(n)
        l = map(int, l.split(","))
        print isValidSudoku(l, n)
