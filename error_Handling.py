#the program handles the error that will occur if the value of 'x' is zero
def divide(x):
    try:
        return 42/x
    except ZeroDivisionError:
        print('Error; Invalid argument.')

print(divide(2))
print(divide(12))
print(divide(0))
print(divide(1))