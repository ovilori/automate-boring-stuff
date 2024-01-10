import re,sys
def email_verification(email):
    email_format = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    atRegex = re.compile(r'[@]')
    atCheck = atRegex.findall(email)

    print(atCheck)
    #ensuring email address has only one occurence of '@'
    if len(atCheck) != 0 and len(atCheck) < 2:
        #return the index (position) of '@' in the email.
        index1 = email.index('@')
        #set the begining of the email domain.
        index = index1 + 1
    else:
        print('Wrong email address format.')
        sys.exit()
    #verify email domain
    if email[index:] in email_format:
        print('Email address is valid.')
    else:
        print('Invalid email address. Please enter a valid email address.')

email_verification('xxxxxxxxxxxx@gmail.com')





