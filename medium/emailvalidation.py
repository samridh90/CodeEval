from sys import argv
import re

#EMAIL_RE = r'^[_a-z0-9-+]+(\.[_a-z0-9-+]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
EMAIL_RE = r'^[^@<>\s\\"]+@[^@.]+(\.[^*@.]+)+$'

def emailValidation():
    ipList = map(str.strip, open(argv[1]).readlines())
    solutions = []
    for ip in ipList:
        if not ip:
            continue
        if not re.match(EMAIL_RE, ip):
            print "false"
            solutions.append("false")
        else:
            print "true"
            solutions.append("true")
    #for solution in solutions:
    #    print solution


if __name__ == '__main__':
    emailValidation()
