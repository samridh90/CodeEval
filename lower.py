import sys


def lowerCase():
    fname = sys.argv[1]
    strList = map(lambda x: x.strip().lower(), open(fname).readlines())
    print "\n".join(strList)
    
if __name__ == "__main__":
    lowerCase()