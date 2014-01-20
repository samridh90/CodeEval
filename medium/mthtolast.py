from sys import argv


def mthToLast():
    fname = argv[1]
    nList = open(fname).readlines()
    for n in nList:
        n = n.strip().split()
        m = int(n.pop()) * -1
        try:
            print n[m]
        except IndexError:
            continue


if __name__ == '__main__':
    mthToLast()
