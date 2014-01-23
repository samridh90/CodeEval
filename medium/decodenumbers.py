from sys import argv


MAX_VAL = 26


def getNumberDecodings(msg):
    if not msg or len(msg) == 1:
        return 1

    count = 0
    num_chrs = 1
    while True:
        chars = msg[:num_chrs]

        if len(chars) != num_chrs:
            break
        if int(chars) > MAX_VAL:
            break

        count += getNumberDecodings(msg[num_chrs:])
        num_chrs += 1

    return count


if __name__ == '__main__':
    ipList = open(argv[1]).readlines()
    for ip in ipList:
        ip = ip.strip()
        print getNumberDecodings(ip)
