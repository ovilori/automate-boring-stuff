'''Simple program to ask a user if they'd like to know how to keep an idiot busy for hours.
If the user answers no, the program quit. If the user answer yes, the program moves to step 1.'''

#import pyinputplus to validate user input.yes
import pyinputplus as pyip

while True:
    message_to_user = 'Do you want to know how to keep an idiot busy for hours?: '

    #call the inputYesNo() function to validate that the user enters yes(y/no(n)
    user_response = pyip.inputYesNo(message_to_user)
    if user_response == 'no':
        break
print('The program will quit now. Have a nice day.')
