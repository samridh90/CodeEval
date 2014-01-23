from sys import argv


def maxSum(triangle, i=0, j=0, h=0):
    #*******recursive*******
    # if i == h:
    #     return triangle[i][j]
    # else:
    #     leftSum = triangle[i][j] + maxSum(triangle, i + 1, j, h)
    #     rightSum = triangle[i][j] + maxSum(triangle, i + 1, j + 1, h)
    #     return max(leftSum, rightSum)
    #******iterative********
    l = len(triangle)
    if l > 1:
        i = l - 2
        while i >= 0:
            row_len = len(triangle[i])
            for j in xrange(row_len):
                val = triangle[i][j]
                triangle[i][j] = max(val + triangle[i+1][j], val + triangle[i+1][j+1])
            i -= 1
    return triangle[0][0]

if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    triangle = []
    for ip in iplist:
        row = map(int, ip.strip().split())
        triangle.append(row)
    #recursive: print maxSum(triangle, 0, 0, len(triangle) - 1)
    print maxSum(triangle)


