from sys import argv

def armstrong():
    fname = argv[1]
    numList = map(str.strip, open(fname).readlines())
    for num in numList:
        l = len(num)
        digits = map(int, list(num))
        s = 0
        for d in digits:
            s += d ** l
        if s == int(num):
            print "True"
        else:
            print "False"


armstrong()