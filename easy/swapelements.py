from sys import argv


def swapElements(l, swappings):
    for swap in swappings:
        i, j = swap
        l[i], l[j] = l[j], l[i]
    return " ".join(l)


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        l, swappings = test.strip().split(":")
        l = l.strip().split()
        temp = swappings.strip().split(", ")
        swappings = map(lambda x: map(int, x.split("-")), temp)
        print swapElements(l, swappings)
    tests.close()
