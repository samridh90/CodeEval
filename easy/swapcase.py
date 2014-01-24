from sys import argv


def swapCase(src):
    res = ""
    for char in src:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            else:
                char = char.upper()
        res += char
    return res


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        print swapCase(test.strip())
    tests.close()
