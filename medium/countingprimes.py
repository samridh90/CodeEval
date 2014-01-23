from sys import argv
from math import sqrt, floor

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    end = int(floor(sqrt(n)))
    for i in xrange(3, end + 1):
        if n % i == 0:
            return False
    return True


def primesBetween(n, m):
    sum = 0
    for i in xrange(n, m + 1):
        if isPrime(i):
            sum += 1
    return sum


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        n, m = map(int, ip.strip().split(','))
        print primesBetween(n, m)
