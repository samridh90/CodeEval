from sys import argv


def simpleSort():
    fname = argv[1]
    numList = open(fname).readlines()
    for n in numList:
        new_n = map(float, n.strip().split())
        new_n.sort()
        print " ".join(map(str, new_n))


if __name__ == '__main__':
    simpleSort()
