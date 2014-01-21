from sys import argv


def trailingString():
    fname = argv[1]
    ipList = map(str.strip, open(fname).readlines())
    solutions = []
    for s in ipList:
        src, dst = s.split(',')
        if dst and src:
            d_end = len(dst) - 1
            s_end = len(src) - 1
            if d_end > s_end:
                solutions.append(0)
            else:
                flag = True
                while d_end >= 0:
                    if src[s_end] != dst[d_end]:
                        flag = False
                        break
                    d_end -= 1
                    s_end -= 1
                if flag:
                    solutions.append(1)
                else:
                    solutions.append(0)
    for solution in solutions:
        print solution

if __name__ == '__main__':
    trailingString()
