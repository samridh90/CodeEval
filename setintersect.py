from sys import argv


def setIntersect():
    fname = argv[1]
    setList = map(lambda x: x.strip().split(";"), open(fname).readlines())
    for sets in setList:
        s1 = set(map(lambda x: int(x), sets[0].split(",")))
        s2 = set(map(lambda x: int(x), sets[1].split(",")))
        print ",".join(map(str, sorted(s1 & s2)))
        
if __name__ == "__main__":
    setIntersect()