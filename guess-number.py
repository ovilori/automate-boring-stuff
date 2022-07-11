import random
secretNumber = random.randint(1,20)
print('Can you guess my secret number correctly? It\'s a number between 1 & 20. Try!')

#allow the user to make six guesses
for guesses in range(1,7):
    guess = int(input('Take a guess: '))

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Great job! You guessed my secret number ' + str(secretNumber) + ', correctly in ' + str(guesses) + ' attempts!')
else: 
    print('You failed to get my secret number correctly. The secret number is ' + str(secretNumber))
statement = 'this \
            is \
            '