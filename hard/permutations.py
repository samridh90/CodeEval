from sys import argv
from itertools import permutations


def printPermutations(s):
    res = []
    for k in permutations(s):
        res.append("".join(k))
    res.sort()
    return res


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = test.strip()
        res = printPermutations(test)
        print ",".join(res)
    tests.close()
