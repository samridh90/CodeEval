from sys import argv


PARENS = {"(": ")", "[": "]", "{": "}"}

def isValidParen(lst):
    stack = []
    for paren in lst:
        if paren in PARENS:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            stack_top = stack.pop()
            if paren != PARENS[stack_top]:
                return False
    if len(stack) != 0:
        return False
    return True


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        ip = list(ip.strip())
        print isValidParen(ip)
