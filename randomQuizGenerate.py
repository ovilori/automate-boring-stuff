#! python3
# randomQuizgenerator - creates quizzes with questions and answers in 
# random order, along with the answer key. 

import random

# the quiz data. Keys are states and values are their capitals.
# states and capitals in Nigeria
nigeria_capitals = {"Abia":	"Umuahia", "Adamawa": "Yola", "Akwa Ibom": "Uyo", "Anambra": "Awka", "Bauchi": "Bauchi", "Bayelsa": "Yenagoa", 
    "Benue": "Makurdi", "Borno": "Maiduguri", "Cross River": "Calabar", "Delta": "Asaba", "Ebonyi": "Abakaliki", "Edo": "Benin City", 
    "Ekiti": "Ado Ekiti", "Enugu": "Enugu", "Gombe": "Gombe", "Imo": "Owerri", "Jigawa": "Dutse", "Kaduna": "Kaduna", "Kano": "Kano", 
    "Katsina": "Katsina", "Kebbi": "Birnin Kebbi", "Kogi": "Lokoja", "Kwara": "Ilorin", "Lagos":	"Ikeja", "Nasarawa": "Lafia", 
    "Niger": "Minna", "Ogun":	"Abeokuta", "Ondo":	"Akure", "Osun": "Oshogbo", "Oyo": "Ibadan", "Plateau":	"Jos", "Rivers": "Port Harcourt", 
    "Sokoto":	"Sokoto", "Taraba":	"Jalingo", "Yobe":	"Damaturu", "Zamfara": "Gusau", "Federal Capital Territory": "Abuja"}

# states and capitals in the united states of america.
usa_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
   'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 
   'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 
   'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 
   'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 
   'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def generate_quiz(capitals, no_of_quiz):
    print('Please wait while we generate the quiz files for your students...')
    # generate the number of quiz files.
    for quizNo in range(no_of_quiz):
        # quiz and answer key files creation
        quizFile = open(f'capitalsquiz{quizNo + 1}.txt', 'w')
        answerKeyFile = open(f'capital_quiz_answers{quizNo + 1}.txt', 'w')

        #header for the quiz
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNo + 1})')
        quizFile.write('\n\n')

        # shuffle the order of the states.

        states = list(capitals.keys())
        random.shuffle(states)
        
        # Loop through all 36 states + FCT, making a question for each
        for questionNum in range(len(capitals)):
            # Get right and wrong answers.
            # save the correct answer
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            # remove the correct answer from the wrong answers list
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            # store the correct answer and three incorrect options
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # write the question and answer options to the quiz file.
            quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
            for i in range(4):
                quizFile.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')

            # write the answer key to a file.
            answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
        
        # close the files.
        quizFile.close()
        answerKeyFile.close()
    print('...................\nDone. Quiz files generated successfully.')


country = int(input("Which country do you want to generate the quiz for? Enter '1' for Nigeria & '2' for USA.\n"))
number_of_quiz = int(input('Enter the number of students taking the quiz.\n'))

if country == 1:
    generate_quiz(capitals=nigeria_capitals, no_of_quiz=number_of_quiz)
elif country == 2:
    generate_quiz(capitals=usa_capitals, no_of_quiz=number_of_quiz)
else:
    print('Kindly enter either 1 or 2 to select the country.')
