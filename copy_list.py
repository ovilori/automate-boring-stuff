#python provides the copy module which includes copy.deepcopy() & copy.copy() function
#to make a duplicate of a mutable value like list or dictionary

#this modifies the original list in place
spam = ['A', 'B', 'C', 'D']
cheese = spam
cheese.append('E')
print(spam)
print(id(spam))
print(cheese)
print(id(cheese))

#this creates a duplicate of a the original list using the copy.copy() function
import copy
spam = ['A', 'B', 'C', 'D']
print('spam: ', spam)
print(id(spam))
cheese = copy.copy(spam)
cheese.append('E')
print('cheese: ', cheese)
print(id(cheese))

#this copies the inner list using the deepcopy() function
spam = ['A', 'B', 'C', 'D', ['another list'], ['another inner list']]
print(id(spam))
#cheese = copy.copy(spam)
cheese = copy.deepcopy(spam)
print(cheese)
print(id(cheese))