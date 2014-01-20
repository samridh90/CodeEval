from sys import argv

def findChar():
    fname = argv[1]
    strList = map(lambda x: x.strip().split(","), open(fname).readlines())
    for ipstr in strList:
        if ipstr == None or len(ipstr) == 0:
            continue
        s = ipstr[0]
        t = ipstr[1]
        print s.rfind(t)
        
if __name__ == "__main__":
    findChar()