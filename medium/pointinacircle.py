from sys import argv


def isPointInCircle(c1, c2, r, p1, p2):
    cx = (c1 - p1) ** 2
    cy = (c2 - p2) ** 2
    d = cx + cy
    rsq = r ** 2
    return d <= rsq


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        l = ip.strip().split(";")
        points = []
        for i in l:
            p = i.split(":")
            points.append(eval(p[1].strip()))
        t = isPointInCircle(points[0][0], points[0][1], points[1], points[2][0], points[2][1])
        print "true" if t else "false"
