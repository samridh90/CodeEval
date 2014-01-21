from sys import argv


def isPalin(s):
    return s == s[::-1]


def palindromSum():
    fname = argv[1]
    ipList = open(fname).readlines()
    solutions = []
    for n in ipList:
        count = 0
        palin = isPalin(n)
        while not palin:
            i = int(n)
            j = int(n[::-1])
            s = str(i + j)
            count += 1
            palin = isPalin(s)
            n = s
        solutions.append((count, s))
    for s in solutions:
        print s[0], s[1]


if __name__ == '__main__':
    palindromSum()
