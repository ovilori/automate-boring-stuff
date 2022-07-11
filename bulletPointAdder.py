#python3

#program to add bullets to Wiki Markup
#adds Wikipedia bullet points to the start of each line of text on the clipboard.
import pyperclip

#get text from the clipboard
text_to_paste = pyperclip.paste() #returns all text on the clipboard.

#seperate lines and add stars. 
lines = text_to_paste.split('\n') #returns a list containing the pasted strings.
#loop through all the indexes in the returned list.
for text in range(len(lines)):
    #adds a star to the each string in the returned list.
    lines[text] = '* ' + lines[text]
#use the join() method to convert from list to string
text_to_paste = '\n'.join(lines)
pyperclip.copy(text_to_paste)
