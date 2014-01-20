from sys import argv

def nmodm():
    fname = argv[1]
    numList = map(lambda x: x.strip().split(","), open(fname).readlines())
    for num in numList:
        a = int(num[0])
        b = int(num[1])
        d = a // b
        r = a - (b * d)
        print r


nmodm()