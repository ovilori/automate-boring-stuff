#This program poses 10 multiplication problems to the user, where the valid input is the problem's correct answer.
#For each question, the user has 10 seconds and 3 attempts to provide the correct answer.
import random, time

#function containing the quiz that will be displayed to the user.
def displayQuiz():

    #variables   
    no_of_questions = 10 #number of questions the program asks
    correctAnswers = 0 #keep track of how many correct answers the user provides
    max_attempt = 3 #set number of attempt/question
    timeout = int(time.perf_counter()) #timeout in seconds

    for questionNo in range(no_of_questions):
        
        #chose a one-digit number and a two-digit number as multiplication problem for the user to solve
        first_no = random.randint(0,9)
        second_no = random.randint(0, 9)

        #calculate and store the quiz answer in a variable
        quiz_answer = first_no * second_no
        for i in range(max_attempt):
            #display the multiplication problem to the user
            user_answer = input(f'{questionNo + 1}. {first_no} x {second_no} = ')
            #validate user's input is only integers.
            if user_answer.strip().isnumeric() == False or user_answer.strip() == '':
                print('Blank values and non integers are incorrect answers.')
            elif int(user_answer) == quiz_answer:
                print('You answered correctly.')
                correctAnswers += 1
                time.sleep(1)
                break
            elif int(user_answer) != quiz_answer:
                print('Incorrect answer.') 
        else:
            print('Limit reached.') 

    #pause for 2 seconds after each question for the user to see the result.
    time.sleep(1)
    print(f'You answered {correctAnswers} question(s) correctly out of {no_of_questions} questions.')  

#main program that calls the displayQuiz() function
while True:
    prompt = input('Ready to answer 10 multiplication problems in 10 seconds & 3 attempts for each question? (enter Yes/y or No/n): ')
    prompt = prompt.lower()
    if prompt == 'yes' or prompt == 'y':
        print('Get ready...')
        time.sleep(1)
        displayQuiz()
    elif prompt == 'no' or prompt == 'n':
        print('Ooops, seems you are not ready for this simple challenge. Thank you.')
        break
    else:
        print('Invalid input. Please enter yes/y, or no/n.')

