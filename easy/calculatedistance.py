from sys import argv
from math import sqrt

def distance(p1, p2):
    return int(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def calculateDistance(src):
    p1, p2 = src.split(") (")
    p1 = map(int, p1.strip("(").split(","))
    p2 = map(int, p2.strip(")").split(","))
    return distance(p1, p2)

if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        print calculateDistance(test.strip())
    tests.close()
