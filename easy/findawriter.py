from sys import argv


def findWriter(src):
    src, key = src.split('|')
    key = map(int, key.strip().split())
    res = ""
    for var in key:
        res += src[var - 1]
    return res


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        print findWriter(test.strip())
    tests.close()
