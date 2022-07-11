#collatz sequence
#program that allows the user type in an integer and that
#keeps calling collatz()  on that number until the function returns the value 1.
def collatz(number):
    #checks if the number is even
    if number % 2 == 0:
        return number // 2
    #checks if the number is odd
    elif number % 2 == 1:
        return 3 * number + 1
try:
    user_input = int(input ('Please enter a  value: '))
    #calls the collatz function until the return value is 1
    while user_input != 1:
        user_input = collatz(user_input)
        print(user_input)
except ValueError:
    print('Your input must be an integer!')
 
