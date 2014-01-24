from sys import argv


def translateString(s):
    mapping = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4',
               'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
    res = ""
    for char in s:
        if char in mapping:
            res += mapping[char]
        elif char.isdigit():
            res += char
    return res if res else "NONE"


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        print translateString(test.strip())
    tests.close()
