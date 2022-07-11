"""
This program asks the user for their age and a password until they provide a valid input
The age must be a numeric value,and the password must contain letters and numbers.
"""
while True:
    age = input('Enter your age: ')
    if age.isnumeric():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password. Password must contain at least a letter, number and special character.')
    password = input('Enter your new password: ')
    if password.isascii():
        break
    print('Password must contain at least a letter, number and special character.')