from sys import argv


def shortestPeriod(s):
    period = 1
    l = len(s)
    while period < l:
        if l % period != 0:
            period += 1
            continue
        pattern = s[0:period]
        flag = True
        for i in xrange(0, l, period):
            chunk = s[i:i+period]
            if chunk != pattern:
                flag = False
                break
        if flag:
            break
        period += 1
    return period


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = test.strip()
        print shortestPeriod(test)
    tests.close()

