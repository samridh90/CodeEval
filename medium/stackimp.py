from sys import argv

def stackImplementation():
    fname = argv[1]
    nList = open(fname).readlines()
    for n in nList:
        n = n.strip().split()
        flag = True
        while n:
            i = n.pop()
            if flag:
                print i,
            flag = not flag
        print ""


if __name__ == '__main__':
    stackImplementation()
