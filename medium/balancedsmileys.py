from sys import argv


def isBalanced(src, paren_count):
    if paren_count < 0:
        return False
    if not src:
        return paren_count == 0
    pair = src[:2]
    if pair == ":)":
        return isBalanced(src[2:], paren_count) or isBalanced(src[2:], paren_count - 1)
    elif pair == ":(":
        return isBalanced(src[2:], paren_count) or isBalanced(src[2:], paren_count + 1)
    else:
        if src[0] == "(":
            return isBalanced(src[1:], paren_count + 1)
        elif src[0] == ")":
            return isBalanced(src[1:], paren_count - 1)
        else:
            return isBalanced(src[1:], paren_count)
    return False


if __name__ == '__main__':
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        res = isBalanced(ip.strip(), 0)
        if res:
            print "YES"
        else:
            print "NO"

