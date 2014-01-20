import math

def printPrimePalin():
    l = [i for i in xrange(0,1001)]
    n = math.ceil(math.sqrt(1000))
    #sieve of eratosthenes
    for i in xrange(2,int(n)+1):
        if l[i] != -1:
            isqr = i * i
            for j in xrange(isqr, 1001, i):
                l[j] = -1
    res = [k for k in l if k != -1 and k != 1 and k != 0]
    #palin check
    for i in reversed(res):
        s = str(i)
        if s == s[::-1]:
            print s
            break

printPrimePalin()