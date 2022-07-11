#This program will listall files in a folder that ends with a suffix specified by the user.
#It will also get the size of each file, and calculate the total size of all files in that folder that ends with the specified suffix.
import os
from pathlib import Path
folder = input('Enter the absolute path of the directory (seperated by double backslash): ')
suffix = input('Enter the suffix of the files: ')
#setting the total size to zero
totalsize = 0
#check for path validity
#folder = Path(folder)
#if folder.is_dir() == False:
if os.path.isdir(folder) == False:
    print(f'{folder} does not exist. Please specify a folder that exist.')
else:
    for filename in os.listdir(folder):
        if filename.endswith(suffix):
            #print(filename, os.path.getsize(filename))
            totalsize = totalsize + os.path.getsize(filename)
            print(f'{filename}, size: {os.path.getsize(filename)}')
    print(f'Total size of files that ends with {suffix}: {totalsize} bytes.')
