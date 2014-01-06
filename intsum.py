import sys

def fileIntSum():
    fname = sys.argv[1]
    print sum(map(lambda x: int(x.strip()), open(fname).readlines()))
    
fileIntSum()