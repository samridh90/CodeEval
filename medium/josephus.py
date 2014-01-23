from sys import argv


def killOrder(n, m):
    arr = [False] * n
    solution = []
    cur = -1
    while not all(arr):
        skip = m
        j = cur
        while skip > 0:
            j = (j + 1) % n
            if arr[j]:
                continue
            else:
                skip -= 1
        arr[j] = True
        solution.append(j)
        cur = j
    return solution


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        n, m = map(int, ip.strip().split(','))
        print " ".join(map(str, killOrder(n, m)))
