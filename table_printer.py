#REWRITEN so in case the sublists values in tableData change, the script won't break


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(Table):
    #First, we get the biggest word for each table or sublist
    collumsSize = []
    for i in range(len(Table)):
        collumsSize.append(len(max(Table[i], key=len)))
    
    #Now, the biggest table, in case of adding or removing a list from the tableData variable
    biggestTable = Table.index(max(Table, key=len))

    #For every index in each sublist of the biggest table 
    for subtable_i in range(len(Table[biggestTable])):
        #For every table in Table or tableData(global scope)
        for table_i in range(len(Table)):
            table = Table[table_i]
            #Checking if the index is bigger than items in the table
            if subtable_i < len(table):
                collum = table[subtable_i].rjust(collumsSize[table_i])
                print(collum, end=" ")
            else:
                #If yes, we add a blank collum
                print("".rjust(collumsSize[table_i]), end=" ")
        print()

printTable(tableData)