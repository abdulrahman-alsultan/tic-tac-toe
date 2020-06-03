import random

board = [' ' for x in range(10)]


def insert(letter, pos):
    if board[pos] == ' ':
        board[pos] = letter
    else:
        print("not empty insert ", pos)


def printBoard(b):
    print('   |   |   ')
    print(b[1], ' |', b[2], '| ', b[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(b[4], ' |', b[5], '| ', b[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(b[7], ' |', b[8], '| ', b[9])
    print('   |   |   ')
    print()


def isEmpty(b):
    if ' ' in b:
        return True
    return False


def isFull(b):
    if ' ' in b:
        return False
    return True


def isWinner(b, l):
    if board[1] == l and board[2] == l and board[3] == l:
        return True
    elif board[1] == l and board[4] == l and board[7] == l:
        return True
    elif board[1] == l and board[5] == l and board[9] == l:
        return True
    elif board[3] == l and board[5] == l and board[7] == l:
        return True
    elif board[4] == l and board[5] == l and board[6] == l:
        return True
    elif board[7] == l and board[8] == l and board[9] == l:
        return True
    elif board[3] == l and board[6] == l and board[9] == l:
        return True
    elif board[2] == l and board[5] == l and board[8] == l:
        return True
    else:
        return False


def Pmove(b):
    x = input("Please select a position to place an 'X' (1-9) :")
    while not x.isnumeric():
        print(" maybe you entered negative number or letter")
        x = input("Please select a position to place an 'X' (1-9) :")
    x = int(x)
    i = 0
    while i == 0:
        if 0 >= x or x >= 10:
            print("invalid number ")
            x = input("Please select a position to place an 'X' (1-9) :")
            while not x.isnumeric():
                print(" maybe you entered negative number or letter")
                x = input("Please select a position to place an 'X' (1-9) :")
            x = int(x)
        elif b[x] != ' ':
            print("position not empty ")
            x = input("Please select a position to place an 'X' (1-9) :")
            while not x.isnumeric():
                print(" maybe you entered negative number or letter")
                x = input("Please select a position to place an 'X' (1-9) :")
            x = int(x)
        else:
            insert('X', x)
            i = 1


def select(b):
    x = []
    add = 0
    for i in b:
        if i == ' ':
            x.append(add)
        add += 1
    return x


def willWin(b):
    if b[1] == 'X' and b[2] == 'X' and b[3] == ' ':
        return 3
    elif b[1] == 'X' and b[3] == 'X' and b[2] == ' ':
        return 2
    elif b[3] == 'X' and b[2] == 'X' and b[1] == ' ':
        return 1
    elif b[1] == 'X' and b[4] == 'X' and b[7] == ' ':
        return 7
    elif b[7] == 'X' and b[4] == 'X' and b[1] == ' ':
        return 1
    elif b[1] == 'X' and b[7] == 'X' and b[4] == ' ':
        return 4
    elif b[1] == 'X' and b[5] == 'X' and b[9] == ' ':
        return 9
    elif b[9] == 'X' and b[5] == 'X' and b[1] == ' ':
        return 1
    elif b[9] == 'X' and b[1] == 'X' and b[5] == ' ':
        return 5
    elif b[4] == 'X' and b[5] == 'X' and b[6] == ' ':
        return 6
    elif b[5] == 'X' and b[6] == 'X' and b[4] == ' ':
        return 4
    elif b[4] == 'X' and b[6] == 'X' and b[5] == ' ':
        return 5
    elif b[7] == 'X' and b[8] == 'X' and b[9] == ' ':
        return 9
    elif b[8] == 'X' and b[9] == 'X' and b[7] == ' ':
        return 7
    elif b[9] == 'X' and b[7] == 'X' and b[8] == ' ':
        return 8
    elif b[5] == 'X' and b[2] == 'X' and b[8] == ' ':
        return 8
    elif b[5] == 'X' and b[8] == 'X' and b[2] == ' ':
        return 2
    elif b[2] == 'X' and b[8] == 'X' and b[5] == ' ':
        return 5
    elif b[6] == 'X' and b[9] == 'X' and b[3] == ' ':
        return 3
    elif b[3] == 'X' and b[6] == 'X' and b[9] == ' ':
        return 9
    elif b[9] == 'X' and b[3] == 'X' and b[6] == ' ':
        return 6
    elif b[3] == 'X' and b[5] == 'X' and b[7] == ' ':
        return 7
    elif b[5] == 'X' and b[7] == 'X' and b[3] == ' ':
        return 3
    elif b[3] == 'X' and b[7] == 'X' and b[5] == ' ':
        return 5
    else:
        return 0


def canCWin(b):
    if b[1] == 'O' and b[2] == 'O' and b[3] == ' ':
        return 3
    elif b[1] == 'O' and b[3] == 'O' and b[2] == ' ':
        return 2
    elif b[3] == 'O' and b[2] == 'O' and b[1] == ' ':
        return 1
    elif b[1] == 'O' and b[4] == 'O' and b[7] == ' ':
        return 7
    elif b[7] == 'O' and b[4] == 'O' and b[1] == ' ':
        return 1
    elif b[1] == 'O' and b[7] == 'O' and b[4] == ' ':
        return 4
    elif b[1] == 'O' and b[5] == 'O' and b[9] == ' ':
        return 9
    elif b[9] == 'O' and b[5] == 'O' and b[1] == ' ':
        return 1
    elif b[9] == 'O' and b[1] == 'O' and b[5] == ' ':
        return 5
    elif b[4] == 'O' and b[5] == 'O' and b[6] == ' ':
        return 6
    elif b[5] == 'O' and b[6] == 'O' and b[4] == ' ':
        return 4
    elif b[4] == 'O' and b[6] == 'O' and b[5] == ' ':
        return 5
    elif b[7] == 'O' and b[8] == 'O' and b[9] == ' ':
        return 9
    elif b[8] == 'O' and b[9] == 'O' and b[7] == ' ':
        return 7
    elif b[9] == 'O' and b[7] == 'O' and b[8] == ' ':
        return 8
    elif b[5] == 'O' and b[2] == 'O' and b[8] == ' ':
        return 8
    elif b[5] == 'O' and b[8] == 'O' and b[2] == ' ':
        return 2
    elif b[2] == 'O' and b[8] == 'O' and b[5] == ' ':
        return 5
    elif b[6] == 'O' and b[9] == 'O' and b[3] == ' ':
        return 3
    elif b[3] == 'O' and b[6] == 'O' and b[9] == ' ':
        return 9
    elif b[9] == 'O' and b[3] == 'O' and b[6] == ' ':
        return 6
    elif b[3] == 'O' and b[5] == 'O' and b[7] == ' ':
        return 7
    elif b[5] == 'O' and b[7] == 'O' and b[3] == ' ':
        return 3
    elif b[3] == 'O' and b[7] == 'O' and b[5] == ' ':
        return 5
    else:
        return 0


def Cmove(b):
    em = canCWin(b)
    if em != 0:
        insert('O', em)
    else:
        em2 = willWin(b)
        if em2 != 0:
            insert('O', em2)
        else:
            x = select(b)
            RN = random.randint(0, len(x) - 1)
            em3 = x[RN]
            print(em3)
            insert('O', em3)


board[0] = 'Zero'
PandC = 1
for s in range(9):
    if isWinner(board, 'X'):
        print("con.. X")
        break
    elif isWinner(board, 'O'):
        print("con.. O")
        break
    if PandC == 1:
        Pmove(board)
        printBoard(board)
        PandC = 2
    else:
        Cmove(board)
        printBoard(board)
        PandC = 1
print("thanks for playing ")