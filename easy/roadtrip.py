from sys import argv


def roadTrip(l):
    prev = 0
    l.sort()
    for i, d in enumerate(l):
        cur = l[i]
        l[i] = l[i] - prev
        prev = cur
    return ",".join(map(str, l))


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        cities = test.strip().split(';')
        l = []
        for city in cities:
            if city:
                city = city.strip().split(',')
                l.append(int(city[1]))
        print roadTrip(l)
    tests.close()
