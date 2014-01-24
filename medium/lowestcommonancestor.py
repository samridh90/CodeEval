from sys import argv


tree = {'root': { 'val': 30, 'left': { 'val': 8,
        'left': { 'val': 3, 'left': None, 'right': None},
        'right': { 'val': 20, 'left': { 'val': 10, 'left': None, 'right': None},
        'right': { 'val': 29, 'left': None, 'right': None}}},
        'right': { 'val': 52, 'left': None, 'right': None}}}


def lowestCommonAncestor(a, b):
    path = []
    root = tree['root']
    if a == root['val'] or b == root['val']:
        return root['val']
    path.append(root['val'])
    while root['val'] != a:
        if a < root['val']:
            root = root['left']
        elif a > root['val']:
            root = root['right']
        path.append(root['val'])
    path2 = []
    root = tree['root']
    path2.append(root['val'])
    while root['val'] != b:
        if b < root['val']:
            root = root['left']
        elif b > root['val']:
            root = root['right']
        path2.append(root['val'])
    prev = path[0]
    for x, y in zip(path, path2):
        if x != y:
            return prev
        prev =  x
    return path[-1] if len(path) < len(path2) else path2[-1]


if __name__ == '__main__':
    tests = open(argv[1])
    for test in tests:
        a, b = map(int, test.strip().split())
        print lowestCommonAncestor(a, b)
    tests.close()
