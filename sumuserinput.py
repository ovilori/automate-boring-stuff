#this program leverages the pyinputplus module to validate that the user entered a series of digits that adds up to 10.
#first we right a function to sum up the user input and then pass the function to the inputCustom() function.

import pyinputplus as pyip

#function to sum up user's inputs.
def sumUptoTen(numbers):

    #converting the string entered by the user to a list
    numbersList = list(numbers)

    #converting each item in the list to an integer
    for idx, digit in enumerate(numbersList):
        numbersList[idx] = int(digit)
    
    #raise an exception if the sum of numbers is not equal to 10.
    if sum(numbersList) != 10:
        raise Exception(f'The digits must add up to 10. Sum of digits entered is {sum(numbersList)}.')

        #return the int form of the numbers.
    return int(numbers)
    
#passing the function above to the inputCustom() function
output = pyip.inputCustom(sumUptoTen, prompt='Enter string of numbers that adds up to 10: ' )
print(output)

