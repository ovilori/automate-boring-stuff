catNames = []

while True:
    name = input('Enter the name of cat ' + str(len(catNames) + 1 ) + '. (or enter nothing to exit).: ')
    if name == '':
        break
    #concatenate list
    #catNames = catNames + [name]
    catNames.append(name)
print('The cat names are: ')
for name in catNames:
    print('    ' + name)
