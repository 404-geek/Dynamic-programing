from pprint import pprint

def isfull(board):

    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                return False

    return True


def possibleEntries(board, i, j):

    possibilityArray = {}

    for x in range(1, 10):
        possibilityArray[x] = 0


    # For horizontal entries
    for y in range(0, 9):
        if not board[i][y] == 0:
            possibilityArray[board[i][y]] = 1

    # For vertical entries
    for x in range(0, 9):
        if not board[x][j] == 0:
            possibilityArray[board[x][j]] = 1

    # For squares of three x three
    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6
    for x in range(k, k + 3):
        for y in range(l, l + 3):
            if not board[x][y] == 0:
                possibilityArray[board[x][y]] = 1

    for x in range(1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0

    return possibilityArray

def Sudokusolver(board):

    i,j = 0,0

    poss = {}

    if isfull(board):
        print("Board Solved Successfully!")
        pprint(board)
        return

    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                i=x
                j=y
                break
        else:
            continue
        break

    poss = possibleEntries(board, i, j)

    for i in range(1,10):

        if not poss[i] == 0:
            board[i][j] = poss[i]
            Sudokusolver(board)

    board[i][j] = 0


def main():

    Sudokuboard = [[5, 3, 0, 0, 7, 0, 0, 0, 0],[6, 0, 0, 1, 9, 5, 0, 0, 0],[0 ,9, 8, 0, 0, 0, 0, 6, 0],[8 ,0, 0, 0, 6, 0, 0, 0, 3],[4 ,0, 0, 8, 0, 3, 0, 0, 1],[7 ,0, 0, 0, 2, 0, 0, 0, 6],[0 ,6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5],[0 ,0, 0, 0, 8, 0, 0, 7, 9]]

    Sudokusolver(Sudokuboard)

if __name__ == '__main__':
    main()

