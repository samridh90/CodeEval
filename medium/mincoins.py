from sys import argv

DENOMS = [5, 3, 1]

def getMinCoins(n):
    total = 0
    for i in DENOMS:
        num = n // i
        if num > 0:
            total += num
        n = n - (num * i)
    return total


if __name__ == '__main__':
    ipList = map(int, open(argv[1]).readlines())
    for ip in ipList:
        print getMinCoins(ip)
