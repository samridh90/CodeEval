from sys import argv


def printPascalsTriangle(depth):
    outer = []
    for i in xrange(depth):
        inner = [0] * (i + 1)
        for j in xrange(i + 1):
            if j == 0 or i == j:
                inner[j] = 1
        outer.append(inner)
    for i in xrange(depth):
        for j in xrange(1, i):
            if outer[i][j] == 0:
                outer[i][j] = outer[i-1][j-1] + outer[i-1][j]
    for i in xrange(depth):
        for j in xrange(i + 1):
            print outer[i][j],
    print ""


if __name__ == '__main__':
    iplist = map(int, open(argv[1]).readlines())
    for i in iplist:
        printPascalsTriangle(i)
