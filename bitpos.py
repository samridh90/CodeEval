import sys


def bitPos():
    fname = sys.argv[1]
    numList = map(lambda x: [int(i) for i in x.strip().split(",")], open(fname).readlines())
    for num in numList:
        n, p1, p2 = num[0], num[1], num[2]
        shiftP1 = (n >> (p1-1)) & 1
        shiftP2 = (n >> (p2-1)) & 1
        res = shiftP1 ^ shiftP2
        print "true" if res == 0 else "false"


if __name__ == "__main__":
    bitPos()
        