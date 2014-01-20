from sys import argv
from collections import Counter
from operator import itemgetter

def bStrings():
    fname = argv[1]
    strList = map(str.strip, open(fname).readlines())
    for s in strList:
        c = Counter(s.lower())
        r_sorted_c = sorted(c.iteritems(), key=itemgetter(1), reverse=True)
        m = 26
        count = 0
        for char, freq in r_sorted_c:
            if char.isalpha():
                count += freq * m
                m -= 1
        print count


bStrings()