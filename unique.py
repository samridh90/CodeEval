from sys import argv

def printUniques():
    fname = argv[1]
    numLists = map(lambda x: [int(i) for i in x.strip().split(",")], open(fname).readlines())
    for numList in numLists:
        d = {}
        res = []
        for num in numList:
            if num not in d:
                res.append(str(num))
                d[num] = True
        print ",".join(res)


if __name__ == "__main__":
    printUniques()