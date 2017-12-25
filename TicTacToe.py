'''
Eric Pacheco
12/24/17
'''

import numpy as np

#takes the index of the square that the user wants to change
#then uses that value that is passed in to change it
#it also takes the board grid as a parameter
def changeSquare(row, col, val, board):
    board[row][col] = val

#prints grid
def printGrid(board):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])for row in board]))

#checks if three in a row
#calls the checkDiagonals method and the check rows method
def threeInRow(board):
    #using transpose to check rows and cols
    #transpose turns cols into rows so that it is easier to check
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

#####checks diagonals
def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return 0

###checks the rows
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
        return 0

##prompt both users
def promptUser(playerNum):
    playerChar = 'X'
    if playerNum == 2:
        playerChar = 'O'

    inputStr = raw_input("Player {0} you are {1} type 'quit' to quit or type the row of your square: ".format(playerNum, playerChar))

    return inputStr
##########################################end function section

#make the list
board = [['0'] * 3 for i in range(3)]

#prompt the user
while True:

    p1inputStr = promptUser(1)
    if p1inputStr is "quit":
        exit()
    ##converting string to int
    p1inputRow = int(p1inputStr)
    p1inputCol = int(raw_input("Enter your Column: "))

    changeSquare(p1inputRow, p1inputCol, 'X', board)

    #########now time for player 2

    p2inputStr = promptUser(2)
    if p2inputStr is "quit":
        exit()
    ##converting string to int
    p2inputRow = int(p2inputStr)
    p2inputCol = int(raw_input("Enter your Column: "))

    changeSquare(p2inputRow, p2inputCol, 'O', board)

    printGrid(board)
    if threeInRow(board) != 0:
        if threeInRow(board) == 'X':
            print "congrats player1, you won!"
            exit()
        elif threeInRow(board) == 'O':
            print "congrats player2, you won!"
            exit()









