from sys import argv


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = test.strip().split(',')
        alpha = ",".join(filter(str.isalpha, test))
        digit = ",".join(filter(str.isdigit, test))
        if alpha and digit:
            print alpha + "|" + digit
        elif alpha:
            print alpha
        else:
            print digit
    tests.close()
