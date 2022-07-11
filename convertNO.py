def convertInteger(number):
        return bin(number).replace('0b', '')
        #return hex(number).replace('0x', '')
number = int(input('Enter an integer: '))
#user = int(input('Enter an integer: '))
number = convertInteger(number)
print(number)



