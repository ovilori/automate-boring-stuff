#! python3
import sys
import pyperclip
"""
myclip.py - This is a multi-clipboard program. Messages are associated with a key phrase that
will be copied to the clipboard. 
The command line arguments will be stored in the variable sys.argv.
The first item in the sys.argv list will always be a string
containing the program’s filename ('myclip.py'), and the second item will
be the first command line argument. Here, the first argument is the
key phrase of the message we want to copy to the clipboard."""

text = {'agree':'Yes, I agree. That sounds fine to me',
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

#checking if the command line argument is missing (if the sys.argv list has less than 2 values in it), 
# & displaying a usage message to the user.

if len(sys.argv) < 2:
    print('Usage: python myclip.py [keyphrase] - copy phrase text')
    sys.exit()

#first commmand line argument is the keyphrase. 
#the key phrase is stored as a string in the 'keyphrase' variable.
keyphrase = sys.argv[1]

#copying the right phrase - checking if the keyphrase exists as a key in the 'text dictionary &
#copying it to the clipboard using the pyperclip module.

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}.')
