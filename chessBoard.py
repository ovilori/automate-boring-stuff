#this program takes a modelled chess board as a dictionary argument and returns True or False\
#after checking if the board is valid. Valid board will have exactly one white king & one black king\
#Each player can only have at most 16 pieces, 8 pawns and all pieces must be on a valid space from 1a to 8h\
#detects when a bug has resulted in an improper chess board.

#model of a chess board
chess_board = {'1a':'wrook','1b':'wknight','1c':'wbishop','1d':'wqueen','1e':'wking','1f':'wbishop','1g':'wknight','1h':'wrook',
                '2a':'wpawn','2b':'wpawn','2c':'wpawn','2d':'wpawn','2e':'wpawn','2f':'wpawn','2g':'wpawn','2h':'wpawn',
                '3a':'','3b':'','3c':'','3d':'','3e':'','3f':'','3g':'','3h':'',
                '4a':'','4b':'','4c':'','4d':'','4e':'','4f':'','4g':'','4h':'',
                '5a':'','5b':'','5c':'','5d':'','5e':'','5f':'','5g':'','5h':'',
                '6a':'','6b':'','6c':'','6d':'','6e':'','6f':'','6g':'','6h':'',
                '7a':'bpawn','7b':'bpawn','7c':'bpawn','7d':'bpawn','7e':'bpawn','7f':'bpawn','7g':'bpawn','7h':'bpawn',
                '8a':'brook','8b':'bknight','8c':'bbishop','8d':'bqueen','8e':'bking','8f':'bbishop','8g':'bknight','8h':'brook'}

#function to validate chess board
def isChessBoardValid(board):

    wking, bking, wpieces, bpieces = 0,0,0,0
    wpawns, bpawns, check, position = 0,0,True,[]
    #representing the letters position
    x_axis = ('a','b','c','d','e','f','g','h')
    #representing the numbers position
    y_axis = range(1,9)
    #coordinates of the chessboard, representing the keys for the dictionary
    for letter in x_axis:
        for number in y_axis:
            position.append(str(number) + letter)
    for coordinate, piece in board.items():
        #checking number of white kings
        if piece == 'wking':
           wking += 1
        #checking number of black kings
        if piece == 'bking':
            bking += 1
        #checking number of white pieces for player 1
        if piece.startswith('w'):
            wpieces += 1
        #checking number of black pieces for player 2
        if piece.startswith('b'):
            bpieces += 1
        #checking number of white pawns
        if piece == 'wpawn':
            wpawns += 1
        #checking number of black pawns
        if piece == 'bpawn':
            bpawns += 1
        #check if all pieces is on a valid space from 1a to 8h
        if coordinate not in position:
            print(f'Invalid board. Wrong position for {piece} on {coordinate}. All pieces must be on a space from 1a to 8h')
            check = False
    #validating number of white and black kings to be exactly one
    if wking != 1 or bking != 1:
        print(f'Invalid board. Board does not have exactly one white king and one black king. White kings: {wking}, black king: {bking}')
        check = False
    #validating that each player has at most 16 pieces.
    if wpieces > 16 or bpieces > 16:
        print(f'Invalid board. One player has more than 16 pieces. One player has {wpieces} pieces and the second player has {bpieces} pieces.')
        check = False
    #validating number of white and black pawns to be at most 8 for each player
    if wpawns > 8 or bpawns > 8:
        print(f'Invalid board. One player has more than 8 pawns. One player has {wpawns} pawns and the second player has {bpawns} pawns.')
        check =  False
    #return true or false if board is valid
    if check:
        return True
    else:
        return False
#calling the function
isChessBoardValid(chess_board)


