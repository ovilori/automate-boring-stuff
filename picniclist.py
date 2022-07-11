guestsItems = {'Olamide':{'Small chops': 5, 'Wine': 6},
                'Tonybest':{'Apples':10, 'Water': 4}}

def totalItems(guests, item):
    num = 0
    for k, v in guests.items():
        num = num + v.get(item, 0)
    return num
print('Number of items being brought to the picnic: ')
print('Small chops: ' + str(totalItems(guestsItems, 'Small chops')))
print('Wine:  ' + str(totalItems(guestsItems, 'Wine')))
print('Apples: ' + str(totalItems(guestsItems, 'Apples')))
print('Water: ' + str(totalItems(guestsItems, 'Water')))
