def printOddNums(n):
    return (i for i in xrange(1, n+1, 2))
    
if __name__ == "__main__":
    for j in printOddNums(99):
        print j