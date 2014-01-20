from sys import argv

def hexToDec():
    """
    Can be solved by using a simple conversion formula;
    for a given hex number a, equivalent decimal is:
    a0 * 16 ^ 0 + a1 * 16 ^ 1 + ... + an * 16 ^ n
    where ai can be any of 0-9 and A-F (and a-f), a:10, b:11,
    c:12, ..., f:15
    """
    #we use the in built int function instead.
    fname = argv[1]
    numList = map(str.strip, open(fname).readlines())
    for num in numList:
        print int(num, 16)


hexToDec()