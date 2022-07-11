#This program poses 10 multiplication problems to the user, where the valid input is the problem's correct answer.
#The program also has a timeout of 10 seconds and limit of 2 attempts for the user to provide a correct answer.

import pyinputplus as pyip
import random, time

while True:
    welcome_message = 'Ready to answer 10 multiplication problems in 10 seconds, 2 attempts?: '

    #call the inputYesNo() function to validate that the user enters yes(y/no(n)
    user_response = pyip.inputYesNo(welcome_message)
    if user_response == 'no':
        print('Ooops, seems you are not ready for this simple challenge. Thank you.')
        break

    #variable to keep track of the number of questions the program asks
    no_of_questions = 10

    #variable to keep track of how many correct answers the user provides
    correctAnswers = 0

    #loop to repeatedly pose a random multiplication problem to the user 10 times.
    for questionNo in range(no_of_questions):

        #chose a one-digit number and a two-digit number as multiplication problem for the user to solve
        first_no = random.randint(0,9)
        second_no = random.randint(0, 9)

        #display the multiplication problem to the user
        prompt = f'{questionNo + 1}. {first_no} x {second_no} = '
        
        try:
            #right answers are handled by allowRegexes parameter. the regex ensures that the answer begins and ends with the correct number.
            #wrong answers are handled by blockRegexes parameter with a custome message.

            pyip.inputStr(prompt, allowRegexes=['^%s$' %(first_no * second_no)], 
                        blockRegexes=[('.*', 'Incorrect answer!')], timeout=10, limit=2)
        
        except pyip.TimeoutException:
            print('Your time is up!')
        except pyip.RetryLimitException:
            print('Retry limit reached!')

        else:
            #This block runs if there are no exceptions from the try block.
            print('You answered correctly!')
            correctAnswers +=1
        
        #pause for 2 seconds after each question for the user to see the result.
        time.sleep(2)
    print(f'You answered {correctAnswers} questions correctly out of {no_of_questions} questions.')







