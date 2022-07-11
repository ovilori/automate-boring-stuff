import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and try again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

#random_no = random.randint(1,9)
#fortune = getAnswer(random_no)
#print(fortune)

#print(getAnswer(random.randint(1,9)))
#allow user to input 
user_input = int(input('Enter a number between 1 and 9: '))
user_luck = getAnswer(user_input)
print(user_luck)