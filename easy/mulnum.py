import sys

def numberMultiples():
    fname = sys.argv[1]
    numList = map(lambda x: [int(i) for i in x.strip().split(",")], open(fname).readlines())
    
    for num in numList:
        x = num[0]
        n = num[1]
        if x <= n:
            print n
            continue
        m = x - n
        c = 1
        while m > 0:
            m = m - n
            c = c + 1
        print n * c


if __name__ == "__main__":
    numberMultiples()