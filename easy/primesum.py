import math

def printSum(n):
    l = [i for i in xrange(0,n+1)]
    #m = math.sqrt(n)
    m = n * math.log(n * math.log(n))
    m = math.floor(math.sqrt(m))
    #sieve of eratosthenes
    for i in xrange(2,int(m)+1):
        if l[i] != -1:
            isqr = i * i
            for j in xrange(isqr, n+1, i):
                l[j] = -1
    res = [k for k in l if k != -1 and k != 1 and k != 0]
    print len(res), sum(res[:1000])

printSum(10000)