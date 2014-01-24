from sys import argv


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = int(test)
        print "1" if test % 2 == 0 else "0"
    tests.close()
