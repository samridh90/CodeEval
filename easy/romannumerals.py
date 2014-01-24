from sys import argv


ROMAN = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
DECIMAL = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def convertToRoman(n, res, decs, romans):
    if decs:
        if n < decs[0]:
            return convertToRoman(n, res, decs[1:], romans[1:])
        else:
            return convertToRoman(n - decs[0], res + romans[0], decs, romans)
    else:
        return res


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = int(test)
        print convertToRoman(test, "", DECIMAL, ROMAN)
    tests.close()
