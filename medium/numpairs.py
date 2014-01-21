from sys import argv


def numPairs():
    fname = argv[1]
    ipList = map(str.strip, open(fname).readlines())
    solutions = []
    for ip in ipList:
        l, k = ip.split(";")
        k = int(k)
        l = map(int, l.split(","))
        f = 0
        r = len(l) - 1
        solution = []
        while f < r:
            s = l[f] + l[r]
            if s == k:
                solution.append((l[f], l[r]))
                r -= 1
            elif s < k:
                f += 1
            else:
                r -= 1
        solutions.append(solution)
    for solution in solutions:
        if solution:
            print ";".join(map(lambda x: str(x[0]) + "," + str(x[1]), solution))
        else:
            print "NULL"


if __name__ == '__main__':
    numPairs()
