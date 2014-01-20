from sys import argv


def queryRow(row_col, row_idx):
    return sum(row_col[row_idx])


def queryCol(row_col, col_idx):
    l = len(row_col)
    return sum([row_col[i][col_idx] for i in xrange(l)])


def set_row_val(row_col, row_idx, row_val):
    l = len(row_col[row_idx])
    for i in xrange(l):
        row_col[row_idx][i] = row_val


def set_col_val(row_col, col_idx, col_val):
    l = len(row_col)
    for i in xrange(l):
        row_col[i][col_idx] = col_val


def queryBoard():
    fname = argv[1]
    queries = open(fname).readlines()
    row_col = [[0 for i in xrange(256)] for j in xrange(256)]
    for query in queries:
        cmd = query.strip().split()
        if cmd[0] == "QueryRow":
            row_idx = int(cmd[1])
            print queryRow(row_col, row_idx)
        elif cmd[0] == "QueryCol":
            col_idx = int(cmd[1])
            print queryCol(row_col, col_idx)
        elif cmd[0] == "SetRow":
            row_idx = int(cmd[1])
            row_val = int(cmd[2])
            set_row_val(row_col, row_idx, row_val)
        elif cmd[0] == "SetCol":
            col_idx = int(cmd[1])
            col_val = int(cmd[2])
            set_col_val(row_col, col_idx, col_val)


if __name__ == '__main__':
    queryBoard()
