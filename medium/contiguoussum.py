from sys import argv


def contiguousSum():
    fname = argv[1]
    ipList = map(str.strip, open(fname).readlines())
    solutions = []
    for l in ipList:
        l = map(int, l.split(","))
        max_so_far = l[0]
        max_ending_here = l[0]
        for i in l[1:]:
            max_ending_here = max(i, max_ending_here + i)
            max_so_far = max(max_so_far, max_ending_here)
        solutions.append(max_so_far)
    for s in solutions:
        print s

if __name__ == '__main__':
    contiguousSum()
