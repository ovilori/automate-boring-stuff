import pyinputplus as pyinput

#validate that input is a number greater than/equals to 5
value = pyinput.inputNum('Enter a number: ', min=5)
print(value)

#validate that input is a number greater than 5
value = pyinput.inputNum('Enter a number: ', greaterThan=5)
print(value)

#validate that input is a number greater than/equal to 4 but less than 6
value = pyinput.inputNum('Enter a number: ', min=4, lessThan=6)
print(value)


