from sys import argv

def detectCycle(l):
    while True:
        try:
            top = l.pop(0)
            next_position = l.index(top)
            current = l[0:next_position]
            next = l[(1 + next_position):(1 + next_position + len(current))]
            if current == next:
                current.insert(0, top)
                return current
        except ValueError:
            continue
        except IndexError:
            break

def findCycles():
    fname = argv[1]
    inList = open(fname).readlines()
    for i in inList:
        cycle = detectCycle(i.strip().split())
        if cycle:
            print " ".join(cycle)


if __name__ == '__main__':
    findCycles()
