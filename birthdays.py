# family birthdays

birthdays = {'Alex': 'October 29', 'Polly': 'March 31', 'Arthur': 'June 19', 'Olamide': 'January 13',
             'Solomon': 'December 15'}

while True:
    name = input('Enter a name (blank to quit): ')
    name = name.title()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ', is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        birthdate = input('Enter their birthday here: ')
        birthdate = birthdate.title()
        birthdays[name] = birthdate
        print('Birthday database updated. Thank you.')
        print(birthdays)
