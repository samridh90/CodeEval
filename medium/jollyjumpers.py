from sys import argv
from math import fabs

def jollyJumpers(ip):
    n = ip[0]
    flag_arr = [False] * (n - 1)
    ip = ip[1:]
    l = len(ip)
    for i in xrange(1, l):
        diff = int(fabs(ip[i] - ip[i - 1]))
        if diff < 1 or diff > (n - 1):
            return "Not jolly"
        flag_arr[diff - 1] = True
    if all(flag_arr):
        return "Jolly"
    return "Not jolly"


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        ip = map(int, ip.strip().split())
        print jollyJumpers(ip)
