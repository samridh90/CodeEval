from sys import argv


def arrayAbsurdity():
    ipList = map(str.strip, open(argv[1]).readlines())
    solutions = []
    for ip in ipList:
        n, l = ip.split(';')
        n = int(n)
        l = map(int, l.split(','))
        expected_sum = ((n - 2) * (n - 1)) // 2
        actual_sum = sum(l)
        diff = actual_sum - expected_sum
        solutions.append(diff)
    for solution in solutions:
        print solution


if __name__ == '__main__':
    arrayAbsurdity()
