from sys import argv


def isChainGood(chain):
    if 'BEGIN' not in chain:
        return False
    visited = {k: False for k in chain.keys()}
    next = chain['BEGIN']
    visited['BEGIN'] = True
    while next != 'END':
        if next in visited and not visited[next]:
            visited[next] = True
            next = chain[next]
        else:
            return False
    if not all(visited.values()):
        return False
    return True


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        ip = ip.strip().split(';')
        chain = {}
        for i in ip:
            b, e = i.split('-')
            chain[b] = e
        print "GOOD" if isChainGood(chain) else "BAD"
