#This program uses regular expression to return the website URLs that begin with http:// or https://
import pyperclip, re

#regular expression to find website URLs that begin with http:// or http://
#http://www.example.com

#url = re.compile(r'''(
                    #(^http://)|(^https://)
                    #([a-zA-Z0-9.-]+)
                    #(\.[a-zA-Z0-9]{2,4})
                #)''', re.VERBOSE)

url = re.compile(r'''http://|https://([a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,4})
               ''', re.VERBOSE)

#finding matches in the text on the clipboard.
text = str(pyperclip.paste())
output = url.search(text)
output = url.findall(text)
print(output)
#print(output.group())
'''matches = []
for groups in output:
#for groups in url.findall(text):
    #foundURL = ''.join([groups[1], groups[2], groups[3]])
    #matches.append(foundURL)
    matches.append(groups[0])

if len(matches) != 0:
    #pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No URL found with with http:// or https:// at the begining.')'''
