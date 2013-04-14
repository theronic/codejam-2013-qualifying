ROWS = 4
COLUMNS = 4
T = -100

IN_PROGRESS = -100
X = 1
O = -1
NO_WIN = 0
DRAW = 100

def dump(board):
    print("\n".join(" ".join(map(str, line)) for line in board))
    print("\n")

"""def diagonals(a): # via http://stackoverflow.com/a/10808134/198927
    rows, cols = a.shape
    if cols > rows:
        a = a.T
        rows, cols = a.shape
    fill = numpy.zeros(((cols - 1), cols), dtype=a.dtype)
    stacked = numpy.vstack((a, fill, a))
    major_stride, minor_stride = stacked.strides
    strides = major_stride, minor_stride * (cols + 1)
    shape = (rows + cols - 1, cols)
    return numpy.lib.stride_tricks.as_strided(stacked, shape, strides)
"""

def hasWon(acc, player):
    return acc * player == max(COLUMNS, ROWS)

def testWin(board, player):
    #dump(board)
    # test horizontal win
    # test vertical win
    acc  = [ sum(row) for row in board ]
    if player*COLUMNS in acc:
        return True

    #print("acc #1",acc)

    # test vertical win
    acc  = [ sum(x) for x in zip(*board) ]
    if player*ROWS in acc:
        return True

    #print("acc #2",acc)
    # test diagonal win
    acc = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    if acc == player * max(ROWS, COLUMNS):
        return True
    #print(acc)
    acc1 = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    if acc1 == player * max(ROWS, COLUMNS):
        return True
    #print(acc1)
    """acc, acc1 = 0, 0
    for r in range(ROWS):
        for c in range(COLUMNS):
            print("row %d, column %d, index %d, rindex %d" % (r,c,r*ROWS+c,r*ROWS + COLUMNS - c - 1))
            acc += board[r*ROWS + c]
            acc1 += board[r*ROWS + COLUMNS - c - 1]
    if hasWon(acc, player):
        return True
"""


    return False

def solve(board, blocked):

    """    Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won"""
    # test horizontals
    # test verticals
    # test diagonals
    acc = 0

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
            #print(4*row + index, '=', board[4*row + index])

    print("Case #%d: %s" % (i+1, solve(board, blockedPos)))

    try:
        input() # read empty line
    except:
        pass


    #a, b = map(int, input().split())
    #print("Case #%d: %s" % (i+1, compute(fair, a, b)))