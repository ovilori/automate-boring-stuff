import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and try again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
#print(messages[3])
#print(len(messages))
print(messages[random.randint(0, len(messages) - 1)])