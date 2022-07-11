#this program creates a back and forth, zizag pattern until the user stops the execution of the program.

import time, sys
#no of spaces to indent.
indent = 0 
#checks whether the indent is increasing or not
indentIncreasing = True

try:
    #the main loop
    while True:
        print(' ' * indent, end = '')
        print('********')
        #pause for 0.1 seconds
        time.sleep(0.1)

        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False
        else:
            #decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
