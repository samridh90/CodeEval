import sys

def reverseWords():
    fname = sys.argv[1]
    strList = map(lambda x: x.strip(), open(fname).readlines())
    for ipstr in strList:
        if ipstr == None or len(ipstr) == 0:
            continue
        ripstr = ipstr[::-1]
        l = ripstr.split(" ")
        lm = " ".join([s[::-1] for s in l])
        print lm
        
if __name__ == "__main__":
    reverseWords()