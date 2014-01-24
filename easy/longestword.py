from sys import argv


def longestWord(l):
    return max(l, key=len)


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = test.strip().split()
        print longestWord(test)
    tests.close()
