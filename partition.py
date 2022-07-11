"""The partition() method when called on a string, searches the string it is called on for
the separator string it is passed, and returns a tuple of three substrings
for the “before,” “separator,” and “after” substrings"""

text = 'Hello world!'

print(text.partition('world'))
#splits the string only on the first occurence if the seperator passed occurs multiple times.
print(text.partition('o'))
#if the seperator does not exist, returns the first occurence of the string, and two emtpy strings.
print(text.partition('X'))
#multiple assigment to assing the returned strings to a variable
before, seperator, after = text.partition(' ')
print('Before: ', before, '\n' 'Seperator: ', seperator, '\n' 'After: ', after)