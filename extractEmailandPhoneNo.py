"""#! python3"""
#program to extract phone number and email address from a document.
import pyperclip, re

#regular expression for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\)|\+\d{3}|\(\+\d{3}\))? #nigeria dialing code
    (\s|-|)                                 #seperator
    (0|\(0\)|)                              #check for zero digit
    (\s|-|)                                 #seperator
    (\d{3})                                 #first 3 digits
    (\s|-|)                                 #seperator
    (\d{3})                                 #first 3 digits
    (\s|-|)                                 #seperator
    (\d{4})                                 #last 4 digits
)''', re.VERBOSE)

#regular expression for email address
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                       #username
    @                                       #the @ symbol seperating the username and domain name
    [a-zA-Z0-9.-]+                          #domain name
    (\.[a-zA-Z0-9]{2,4})                    #top-level domain
)''', re.VERBOSE)

#finding matches in the text on the clipboard.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNumber = ''.join([groups[1], groups[3], groups[5], groups[7], groups[9]])
    matches.append(phoneNumber)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#copy the results to the clipboard.
if len(matches) != 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

    