from collections import Counter
from sys import argv

def selfDescribing():
    fname = argv[1]
    numList = map(str.strip, open(fname).readlines())
    for num in numList:
        c = Counter(num)
        flag = False
        for i, n in enumerate(num):
            if int(n) != c[str(i)]:
                flag = True
                break
        if flag:
            print "0"
        else:
            print "1"


selfDescribing()