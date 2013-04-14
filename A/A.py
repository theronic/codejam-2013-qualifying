ROWS = 4
COLUMNS = 4
T = -100 # BLOCKED

X = 1
O = -1

def dump(board):
    print("\n".join(" ".join(map(str, line)) for line in board))

def testWin(board, player):
    # test horizontal win
    acc  = [ sum(row) for row in board ]
    if player*COLUMNS in acc:
        return True

    # test vertical win
    acc  = [ sum(x) for x in zip(*board) ]
    if player*ROWS in acc:
        return True

    # test diagonal win
    acc = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    if acc == player * max(ROWS, COLUMNS):
        return True

    # test the other diagonal win
    acc1 = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    if acc1 == player * max(ROWS, COLUMNS):
        return True

    return False

def solve(board, blocked):
    #test for an X win
    if blocked != (-1,-1):
        board[blocked[0]][blocked[1]] = X

    if testWin(board, X):
        return "X won"

    #test win for player O
    if blocked != (-1,-1):
        board[blocked[0]][blocked[1]] = O

    if testWin(board, O):
        return "O won"

    for row in board:
        if 0 in row:
            return "Game has not completed"

    return "Draw"

def parseChar(c):
    if c == '.':
        return 0
    elif c == 'X':
        return X
    elif c == 'O':
        return O
    elif c == 'T':
        return T

    raise ValueError

nCases = int(input())
for i in range(nCases):
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]

    # read 4 lines
    blockedPos = (-1,-1)
    for row in range(4):
        line = input()
        #print(list(line))
        for index, c in enumerate(line):
            val = parseChar(c)
            if val == -100:
                blockedPos = (row,index)
            board[row][index] = parseChar(c)

    print("Case #%d: %s" % (i+1, solve(board, blockedPos)))

    try:
        input() # read empty line
    except:
        pass