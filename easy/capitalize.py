from sys import argv


def capitalize(src):
    l = src.strip().split()
    res = []
    for word in l:
        c = word[0]
        if c.isalpha() and c.islower():
            word = c.upper() + word[1:]
        res.append(word)
    return " ".join(res)


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        print capitalize(test)
    tests.close()
