from sys import argv


A = "rbcvjnmkfkdyxyqcinarbczjkfoscddewrbcujllmcp"
B = "tcrbksorbyrejpmysljylckdkxveddknmcrejsicpdrysi"
C = "dekrkdeoyakwaejicfkicirezjkr"
A_T = "thepublicisamazedbythequicknessofthejuggler"
B_T = "wethinkthatourlanguageisimpossibletounderstand"
C_T = "soitisokayifyoudecidedtoquit"

def learntDict():
    #learn from example
    alpha = dict(zip(A + B + C, A_T + B_T + C_T))
    #given
    alpha['g'] = 'v'
    #deduced
    alpha['h'] = 'x'
    return alpha


def translate(src, alpha):
    res = ""
    for char in src:
        if char.isalpha():
            res += alpha[char]
        else:
            res += char
    return res


if __name__ == '__main__':
    alpha = learntDict()
    iplist = open(argv[1]).readlines()
    for ip in iplist:
        ip = ip.strip()
        print translate(ip, alpha)
