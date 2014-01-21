from sys import argv
from collections import Counter

def findFirstNonRepeated():
    fname = argv[1]
    ipList = map(str.strip, open(fname).readlines())
    solutions = []
    for word in ipList:
        word = word.lower()
        char_count = Counter(word)
        for char in word:
            if char_count[char] == 1:
                solutions.append(char)
                break
    for s in solutions:
        print s


if __name__ == '__main__':
    findFirstNonRepeated()
