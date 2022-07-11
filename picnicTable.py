
picnicItems = {'Sandwiches': 5, 'Apples': 5, 'Cups': 3, 'Wine': 10, 'Cookies': 500}

def picnic(itemsDico, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, ' '))
    for key,value in itemsDico.items():
        print(key.ljust(leftWidth,' ') + str(value).rjust(rightWidth))
picnic(picnicItems,10,5)
