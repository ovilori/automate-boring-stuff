import random,sys
print ('ROCK, PAPER, SCISSORS')

#keeping track of number of wins, losses and ties

wins = 0
losses = 0
ties = 0

#main loop of the game
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    #the player input loop
    while True:
        print('Enter your move: (r)ock or (p)aper or (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            #quit the program
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            #break out of the player's input loop.
            break
        print('Type one of r, p, s or q.')
    #display the player's choice
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    #display the computer's choice
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    #display and record the win, loss or tie score

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses +1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1


