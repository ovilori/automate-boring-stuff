myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('size' in myCat)
print('size' in myCat.keys())
print('Length: ' + str(len(myCat)))
print(sum(value == 'fat' for value in myCat.values()))
#print(myCat['size'])
#print('My cat size is ' + myCat['size'])
#using values, key and items method
for v in myCat.values():
    print(v)
for k in myCat.keys():
    print(k)
print('Items')
for i in myCat.items():
    print(i)
for k,v in myCat.items():
    print('Key: ' + k + ', '  'Values: ' + v)

picnicItems = {'Apples':'5', 'Cups': '3'}
#the get method
print('I am bringing ' + str(picnicItems.get('Cups', 0)) + ' cups to the picnic.')
#checks whether Wine exists and since it does not exist, returns the specified default value of 2.
print('I am bringing ' + str(picnicItems.get('Wine', 2)) + ' bottles of wine to the picnic.')

#the set default method
picnicItems.setdefault('Wine', '5') #adds 'Wine' as key and '5' as value if it does not exist already.
print(picnicItems)
picnicItems.setdefault('Wine', '3') #returns the key's value since it already exists.
print(picnicItems)

