from sys import argv


def strip_split(s):
    return s.strip().split()

if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        print " ".join(map(str, map(lambda x: int(x[0]) * int(x[1]), zip(*map(strip_split, test.strip().split('|'))))))
    tests.close()
