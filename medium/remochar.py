from sys import argv


def removeChars():
    fname = argv[1]
    ipList = map(str.strip, open(fname).readlines())
    solutions = []
    for s in ipList:
        src, rem = s.split(", ")
        rem_dict = {}
        for r in rem:
            rem_dict[r] = True
        res = ""
        for char in src:
            if char in rem_dict:
                continue
            else:
                res += char
        solutions.append(res)
    for s in solutions:
        print s.strip()


if __name__ == '__main__':
    removeChars()
