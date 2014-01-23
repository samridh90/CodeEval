from sys import argv


def reverseGroups(l, k):
    res = []
    for i in xrange(0, len(l), k):
        temp = l[i:i+k]
        if len(temp) == k:
            for j in reversed(temp):
                res.append(j)
        else:
            for j in l[i:]:
                res.append(j)
    return res


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        l, k = ip.strip().split(';')
        k = int(k)
        l = map(int, l.split(','))
        print ",".join(map(str, reverseGroups(l, k)))
