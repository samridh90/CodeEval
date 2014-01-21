from sys import argv
from math import sqrt, floor

def squareSum():
    fname = argv[1]
    ipList = map(int, open(fname).readlines())
    solutions = []
    for n in ipList[1:]:
        limit = int(floor(sqrt(n)))
        arr = [i * i for i in xrange(limit + 1)]
        count = 0
        f = 0
        r = len(arr) - 1
        while f <= r:
            s = arr[f] + arr[r]
            if s == n:
                count += 1
                r -= 1
            elif s < n:
                f += 1
            else:
                r -= 1
        solutions.append(count)
    for solution in solutions:
        print solution


if __name__ == '__main__':
    squareSum()
