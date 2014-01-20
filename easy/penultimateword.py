from sys import argv


def penultimateWord():
    fname = argv[1]
    senList = open(fname).readlines()
    for sentence in senList:
        broken = sentence.strip().split()
        print broken[-2]

if __name__ == '__main__':
    penultimateWord()
