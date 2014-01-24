from sys import argv
from collections import Counter


def getLowestUnique(l):
    counter = Counter(l)
    m = 10
    idx = 0
    for n, i in enumerate(l):
        if counter[i] == 1 and i < m:
            m = i
            idx = n + 1
    return idx


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = map(int, test.strip().split())
        print getLowestUnique(test)
    tests.close()
