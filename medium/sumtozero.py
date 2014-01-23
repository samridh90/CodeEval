from sys import argv
from itertools import combinations


def sumToZero(l, n=4):
    if len(l) < n:
        return 0
    count = 0
    for c in combinations(l, n):
        if sum(c) == 0:
            count += 1
    return count


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        l = map(int, ip.strip().split(','))
        print sumToZero(l)
