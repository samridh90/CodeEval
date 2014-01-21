from sys import argv
from collections import Counter

def pangram():
    ipList = map(str.strip, open(argv[1]).readlines())
    solutions = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ip in ipList:
        ip = ip.lower()
        char_count = Counter(ip)
        res = ""
        for char in alphabet:
            if char not in char_count:
                res += char
        if res:
            solutions.append(res)
        else:
            solutions.append("NULL")
    for solution in solutions:
        print solution

if __name__ == '__main__':
    pangram()
