from sys import argv
from itertools import combinations

def findDistance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def isSquare(l):
    d = {}
    for pair in combinations(l, 2):
        distance = findDistance(*pair)
        if distance in d:
            d[distance].append(pair)
        else:
            d[distance] = [pair]
    if len(d.keys()) == 2:
        return True
    return False


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        l = map(eval, ip.strip().split(', '))
        t = isSquare(l)
        print "true" if t else "false"
