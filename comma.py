"""This function takes a list value as an argument and return a string with all the items seperated by a comman and a space"""
def list_to_string(list):
    #checking if an empty list is passed.
    if len(list) == 0:
        print('Operation cannot be performed on an empty list.')
    #converting to string and inserting ', and' before the last item in the list.
    else:
        string = ', '.join(list[0:-2]) + ', ' + ', and '.join(list[-2:])
        print(string)
#example
spam = ['apples', 'bananas', 'tofu', 'cats', 'dog', 'table', 'chairs']
list_to_string(spam)

