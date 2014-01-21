from sys import argv


def numOfOnes():
    fname = argv[1]
    ipList = map(int, open(fname).readlines())
    solutions = []
    for i in ipList:
        count = 0
        while i != 0:
            if (i & 1) == 1:
                count += 1
            i = i >> 1
        solutions.append(count)
    for solution in solutions:
        print solution


if __name__ == '__main__':
    numOfOnes()
