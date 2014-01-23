from sys import argv
from urllib2 import unquote
import re

URI = r'^(?P<scheme>[^:]+):\/\/(?P<host>[^:\/]+)(:(?P<port>\d+)?)?(?P<path>\/.*)?$'


def areEquivalent(url1, url2):
    url1 = unquote(url1)
    url2 = unquote(url2)
    m1 = re.match(URI, url1)
    d1 = {'scheme': m1.group('scheme').lower(), 'host': m1.group('host').lower(),
          'port': m1.group('port') or '80', 'path': m1.group('path')}
    m2 = re.match(URI, url2)
    d2 = {'scheme': m2.group('scheme').lower(), 'host': m2.group('host').lower(),
          'port': m2.group('port') or '80', 'path': m2.group('path')}
    return d1 == d2


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        u1, u2 = ip.strip().split(';')
        print areEquivalent(u1, u2)

