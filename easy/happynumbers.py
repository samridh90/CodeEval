from sys import argv


def sumOfSqrDigits(n):
    return sum(map(lambda x: int(x) ** 2, list(n)))

def happyNumbers():
    fname = argv[1]
    numList = map(lambda x: x.strip(), open(fname).readlines())
    for num in numList:
        d = {}
        t = frozenset(num)
        flag = False
        while t not in d:
            d[t] = True
            s = sumOfSqrDigits(num)
            if s == 1:
                flag = True
                break
            num = str(s)
            t = frozenset(num)
        if flag:
            print "1"
        else:
            print "0"


if __name__ == "__main__":
    happyNumbers()