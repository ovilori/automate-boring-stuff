#program below counts the occurence of each character in a string.
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#message = message.lower()
#print(message)
count = {}
for character in message.lower():
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)