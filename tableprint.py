#this function takes a list of strings and displays it in a well-organized table with each column right-justified.
def arrangeTable(table):
    #finding the longest string in each list
    colwidths = [0] * len(table)
    for list in range(len(table)):
        for string in table[list]:
            if colwidths[list] < len(string):
                colwidths[list] = len(string)

#looping through the table 
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colwidths[y]), end = '  ')
        print()

#sample table
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose'],
['mice', 'elephant', 'room', 'staircase']]

#calling the function
arrangeTable(tableData)


