'''Learning about working with file directory here'''
from pathlib import Path
import sys, os

#print(Path('spam', 'bacon', 'eggs'))

homeFolder = r'C:Users\Olamide\AI'
subFolder = 'spam'
fullPath = Path(homeFolder) / Path(subFolder)

#print(fullPath)
#p = Path.cwd()
#print(p)
#os.chdir(#enter path here) #changing directory
#print(p)
#print(p.is_absolute())

#print(sys.platform]=   )
#print(Path.home())

myFiles = ['accoounts.txt', 'details.csv', 'invite.docx']
#for filename in myFiles:
    #print(Path(Path.cwd(), filename))
p = Path('C:/Users/\'Lamide\Ilori/Python/network-python/ftp_user_pw_cracker.py')
#print(p.anchor)
#print(p.parent)
#print(p.name)
#print(p.stem)
#print(p.suffix)
#print(p.drive)
#print(p.parents[0])
#print(p.parents[1])

#returns the name of the file
#print(os.path.basename(p))
#returns the name of the file directory
#print(os.path.dirname(p))
#returns the path directory and base name together
#print(os.path.split(p))
#getting the size of the file
#print(os.path.getsize('C:Users\\\'Lamide Ilori\\Python\\network-python\\ftp_user_pw_cracker.py'))

'''
#print all files in a folder wthat ends with a particluar suffix, their sizes and total size of such  file.
#print(os.listdir(folder))
folder = 'C:\\Users\\\'Lamide Ilori\\Python\\automate-borring-stuffs'
total = 0
for file in os.listdir(folder):
    if file.endswith('py'):
        #print(file, os.path.getsize(file))
        total = total + os.path.getsize(file)
        print(f'{file}, size: {os.path.getsize(file)}')
print(f'Total size of files that ends with py: {total}')
'''
#list of files using glob patterns
folder = Path('C:/Users/\'Lamide\Ilori/Desktop')
for filename in folder.glob('*.xlsx'):
    print(filename)



