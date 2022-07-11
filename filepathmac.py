from pathlib import Path
import os, sys
from shlex import shlex
print(Path('spam', 'bacon', 'eggs'))
#print(sys.platform)

#using the / operator to Join paths - replaces the older os.path.join() function.
homeFolder = Path('/Users/olamideilori')
subFolder = Path('spam')
print(homeFolder/subFolder)

#current working directory
print(Path.cwd())

# home directory
print(Path.home())

# returns a string of a relative path from the start path to path.
print(os.path.relpath(subFolder,homeFolder))

# returns a string of the absolute path of the argument.
print(os.path.abspath('.'))

# returns True if the argument is an absolute path and False if it is a relative path
print(os.path.isabs('.'))

p = Path('/Users/olamideilori/spam.txt')
print(p.anchor)
print(p.parent) # This is a Path object, not a string. WindowsPath('C:/Users/Al')
print(p.name)
print(p.stem)
print(p.suffix)

print('/Users/olamideilori/spam.txt'.split(os.sep))

# return the size in bytes of the file in the path argument
print(os.path.getsize('./copy_list.py'))

# return a list of filenmae strings for each file in the path argument
# print(os.listdir('.'))

# size of each of the files in the current directory and total size
totalSize = 0
for filename in os.listdir('.'):
    filesize = os.path.getsize(os.path.join('.',filename))
    totalSize = totalSize + filesize
    # print(f'{filename}, {filesize} bytes')
# print(f'Total size: {totalSize}')

# using glob patterns: *, ?
# return all files in the path
p = Path('.')
# print(list(p.glob('*')))

# returns all the files that have the extension .txt
p = Path('.')
# print(list(p.glob('*.txt')))

# opening files with the open() function
opentext = open('/Users/olamideilori/Documents/study/automate-boring-stuff/newtext.txt')

# reading contents of files
# print(opentext.read())

# using readlines to get a list of string values from the file
# print(opentext.readlines())

# writing to files
opentext = open('newtext.txt', 'w')
opentext.write('Hello, Africa!\n')
opentext = open('newtext.txt', 'a')
opentext.write('Hello, Nigeria!\n')
opentext.close()
opentext = open('newtext.txt')
open_text = opentext.read()
opentext.close()
# print(open_text)

# using the shelve module to save variables
# use shelve module to save data from Python programs.
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
animals = ['Dogs', 'Snakes', 'Goats']
shelfFile['cats'] = cats
shelfFile['animals'] = animals
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
print(shelfFile['animals'])

# saving variables using the pprint.pformat() function
import pprint
cats = [
    {
        'name': 'Zophie',
        'desc': 'chubby'
    },
    {
        'name': 'Pooka',
        'desc': 'fluffy'
    }
]
cats = pprint.pformat(cats)
# print(cats)

fileobj = open('mycats.py', 'w')
fileobj.write('cats = ' + cats + '\n')
fileobj.close()

# import te saves file
import mycats
print(mycats.cats)
print(mycats.cats[1]['desc'])
