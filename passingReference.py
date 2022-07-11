#values of arguments are copied to the parameter variables when a function is called
#For lists (and dictionaries), a copy of the reference is used for the parameter.
#in the code below, spam & someParameter refer to the same list, although they contain seperate references.


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
print(id(spam))
eggs(spam)
print(spam)
print(id(spam))

