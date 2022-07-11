#data structure to represent the tic-tac-toe board.
the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'middle-L': ' ', 'middle-M': ' ', 'middle-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#function to display the tic-tac-toe board
def printBoard(board):
    print('The tic-tac-toe board:' + '\n')
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['middle-L'] + '|' + board['middle-M'] + '|' + board['middle-R'])
    print('-+-+-') 
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('\n')
#player moves
turn = 'X'
for i in range(9):
    printBoard(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(the_board)