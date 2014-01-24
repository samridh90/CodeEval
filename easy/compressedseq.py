from sys import argv


def compressSequence(seq):
    l = len(seq)
    res = []
    i = 0
    while i < l:
        cur = seq[i]
        count = 0
        end = False
        while seq[i] == cur:
            i += 1
            count += 1
            if i >= l:
                end = True
                break
        res.append(count)
        res.append(cur)
        if end:
            break
    return " ".join(map(str, res))


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = test.strip().split()
        print compressSequence(test)
    tests.close()

