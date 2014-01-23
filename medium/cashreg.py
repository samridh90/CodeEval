from sys import argv

CHANGE = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
STRINGS = {10000: "ONE HUNDRED", 5000: "FIFTY", 2000: "TWENTY",
           1000: "TEN", 500: "FIVE", 200: "TWO", 100: "ONE",
           50: "HALF DOLLAR", 25: "QUARTER", 10: "DIME",
           5: "NICKEL", 1: "PENNY"}

def makeChange(change):
    res = []
    for c in CHANGE:
        n = change // c
        if n > 0:
            for i in xrange(int(n)):
                res.append(STRINGS[c])
            change = change - (c * n)
    return res


def tocents(s):
    dollars, cents = s.split('.')
    return int(dollars) * 100 + int(cents)


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        pp, ch = map(float, ip.strip().split(";"))
        change = ch - pp
        if change < 0:
            print "ERROR"
        elif change == 0:
            print "ZERO"
        else:
            change = tocents(str(change))
            print ",".join(map(str, makeChange(change)))
