def dump(board):
    print("\n".join(" ".join(map(str, line)) for line in board))

def solve(board, n,m):
    #dump(board)

    rows = [max(row) for row in board]
    #print(rows)

    cols = [max(col) for col in zip(*board)]
    #print(cols)

    for r, row in enumerate(rows):
        for c, col in enumerate(cols):
            val = board[r][c]
            #print("v:",val, max(row,col))
            if val < min(row,col):
                return "NO"
            #print(board[r][c],',', end="")
        #print("")
        #print("\n")

    """
    for row in range(1,n+1):
        for col in range(1,m+1):
            val = board[row][col]

            above = board[row-1][col]
            below = board[row+1][col]
            left = board[row][col-1]
            right = board[row][col+1]

            # check above and below, check left and right, check corners (above, left) (above, right) (below, left) (below, right)
            if (((above == 0 or above == val) and (below == 0 or below == val))
                or ((left == 0 or left == val) and (right == 0 or right == val))
                or ((left == 0 or left == val) and (below == 0 or below == val))
                or ((right == 0 or right == val) and (below == 0 or below == val))
                or ((right == 0 or right == val) and (above == 0 or above == val))
                or ((left == 0 or left == val) and (above == 0 or above == val))

                # corners
                or (above == 0 and left == 0)
                or (above == 0 and right == 0)
                or (below == 0 and right == 0)
                or (below == 0 and left == 0)):
                    continue
            else:
                print("failed at %d,%d with %d" % (row,col,val))
                return "NO"

    """

    return "YES"

T = int(input())
for i in range(T):
    N,M = map(int, input().split())

    #row = [0 for _ in range(M)]
    #board = [row for _ in range(N)]
    #print(board)

    board = []

    for row in range(N):
        board.append(list(map(int, input().split())))

    #board.append([0 for _ in range(M+2)])

    print("Case #%d: %s" % (i+1, solve(board, N,M)))

        #a, b = map(int, input().split())
        #print("Case #%d: %s" % (i+1, compute(fair, a, b)))