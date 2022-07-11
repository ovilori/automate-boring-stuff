#program that recommmends a car based on the temperature value of the location entered by a user.
#storing types of cars in a dictionary
cars = {'Car_A':'Convertible', 'Car_B':'SUV', 'Car_C':'Truck'}

#accepting user input
temp = int(input('What is the temperature of the location you plan to visit?: '))

#select Convertible if temperature is greater than 80.
if temp > 80:
    car = cars['Car_A']
    print(f'A {car} is recommended for a temperature value of {temp}.')

#select Truck if temperature is less than 60.
elif temp < 60:
    car = cars['Car_C']
    print(f'A {car} is recommended for a temperature value of {temp}.')

#select SUV if temperature is greater than 60 or less than 80.
else:
    car = cars['Car_B']
    print(f'A {car} is recommended for a temperature value of {temp}.')


