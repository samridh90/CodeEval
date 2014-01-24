from sys import argv


MAPPING = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
           'nine': '9', 'zero': '0'}


def wordToDigit(wordList):
    res = ""
    for word in wordList:
        if word in MAPPING:
            res += MAPPING[word]
    return res

if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        test = test.strip().split(';')
        print wordToDigit(test)
    tests.close()
