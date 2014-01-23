from sys import argv


def isOverlapping(blx1, bly1, trx1, try1, blx2, bly2, trx2, try2):
    l = max(blx1, blx2)
    r = min(trx1, trx2)
    b = max(bly1, bly2)
    t = min(try1, try2)
    if l <= r and b <= t:
        return True
    return False


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        c = map(int, ip.strip().split(','))
        blx1, bly1, trx1, try1 = c[0], c[3], c[2], c[1]
        blx2, bly2, trx2, try2 = c[4], c[7], c[6], c[5]
        print isOverlapping(blx1, bly1, trx1, try1, blx2, bly2, trx2, try2)
