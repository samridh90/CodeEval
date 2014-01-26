from sys import argv


def longestCommonSubsequence(a, b):
    m = len(a)
    n = len(b)
    L = [[0 for i in xrange(n + 1)] for j in xrange(m + 1)]
    i = m
    while i >= 0:
        j = n
        while j >= 0:
            if i == m or j == n:
                L[i][j] = 0
            elif a[i] == b[j]:
                L[i][j] = 1 + L[i+1][j+1]
            else:
                L[i][j] = max(L[i+1][j], L[i][j+1])
            j -= 1
        i -= 1
    lcs_length = L[0][0]
    res = ""
    i = 0
    j = 0
    while i < m and j < n:
        if a[i] == b[j]:
            res += a[i]
            i += 1
            j += 1
        elif L[i+1][j] >= L[i][j+1]:
            i += 1
        else:
            j += 1
    return res



if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        a, b = test.strip().split(";")
        print longestCommonSubsequence(a, b)
    tests.close()
