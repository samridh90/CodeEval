import sys

def fizzbuzz():
    fname = sys.argv[1]
    f = open(fname)
    args = map(lambda x: [int(i) for i in x.strip().split()], f.readlines())
    for arg in args:
        printFizzBuzz(arg[0], arg[1], arg[2])
        print ""


def printFizzBuzz(a, b, n):
    for i in xrange(1, n+1):
        res = ""
        if i % a == 0:
            res += "F"
        if i % b == 0:
            res += "B"
        if res:
            print res,
        else:
            print i,
    
if __name__ == "__main__":
    fizzbuzz()          