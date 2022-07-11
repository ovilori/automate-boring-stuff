#using the global statement to modify the value of a variable 
#inside a function

""" def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs) """

""" def spac():
    print(eggs)
eggs = 45
spac()
print(eggs) """

def spam():
   global eggs 
   eggs = 'spam'
   #print(eggs)
def bacon():
    eggs = 'global'
def ham():
    print(eggs)
eggs = 42
spam()
print(eggs)
