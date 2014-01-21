from sys import argv


def decToBin():
    fname = argv[1]
    ipList = map(str.strip, open(fname).readlines())
    solutions = []
    for i in ipList:
        res = ""
        i = int(i)
        if i == 0:
            res = "0"
        else:
            while i != 0:
                res += str(i & 1)
                i = i >> 1
        solutions.append(res[::-1])

    for s in solutions:
        if s:
            print s

if __name__ == '__main__':
    decToBin()
