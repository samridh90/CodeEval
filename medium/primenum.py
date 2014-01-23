from sys import argv
from math import sqrt, floor

def nPrimes(n):
    candidates = [True for i in xrange(n+1)]
    try:
        candidates[0] = False
        candidates[1] = False
    except IndexError:
        return []
    sqrt_n = long(floor(sqrt(n)))
    for i in xrange(2, sqrt_n + 1):
        if candidates[i]:
            j = i * i
            while j <= n:
                candidates[j] = False
                j += i
    return [str(i) for i, k in enumerate(candidates) if k == True]


if __name__ == '__main__':
    ipList = map(long, open(argv[1]).readlines())
    for ip in ipList:
        ans = nPrimes(ip)
        if ans:
            print ",".join(ans)

