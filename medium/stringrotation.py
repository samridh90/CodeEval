from sys import argv


def isSubstr(src, tst):
    return src.find(tst) != -1


def isRotation(src, tst):
    src += src
    return isSubstr(src, tst)


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        src, tst = ip.strip().split(',')
        print isRotation(src, tst)
