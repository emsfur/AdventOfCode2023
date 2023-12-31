# if given an input of a single found in the schematic (the index within the matrix),
# getFullNum returns the rest of the number connected to that single int
def getFullNum(iNum, jNum):
    # add the original int to the output
    num = data[iNum][jNum]

    stopLeft = False
    stopRight = False

    # looking at the example and puzzle input, art numbers only span 3 chars max
    # so we check 3 characters out on both sides (left/right) of our number and add it to the output properly
    for k in range(1,3):

        # checking the right side of our number and adds it to the right of num
        if ( data[iNum][jNum+k].isdigit() and not stopLeft):
            num += data[iNum][jNum+k]
        else:
            stopLeft = True
        
        # checking left side of our number and adds it to the left of num
        if (data[iNum][jNum-k].isdigit() and not stopRight):
            num = data[iNum][jNum-k] + num
        else:
            stopRight = True

    return num

# given the location of a symbol within the matrix, 
# getPatNums will return all adjacent part numbers
def getPartNums(iSymbol, jSymbol):
    partNums = []

    # checking adjacent numbers without having unvalid duplicates added has to be accounted for     # EX:
    # this is only an issue on the top and bottom where the number centers with the symbol          # 123...  
                                                                                                    # .*....
    # if the top middle has a number                                                                # ..123.  
    if ( data[iSymbol - 1][jSymbol].isdigit() ):   
        # check if the top left/right is one connected to the same number                                                  
        if ( data[iSymbol - 1][jSymbol - 1].isdigit() ):
            num = getFullNum(iSymbol - 1, jSymbol - 1)
            partNums.append(num)  
        elif ( data[iSymbol - 1][jSymbol + 1].isdigit() ):
            num = getFullNum(iSymbol - 1, jSymbol + 1)
            partNums.append(num)
        else:  # else just add the number that's there above the symbol    
            num = getFullNum(iSymbol - 1, jSymbol)
            partNums.append(num)
    else:
        # accounts for two seperate numbers with corners of number adjacent to symbol
        if ( data[iSymbol - 1][jSymbol - 1].isdigit() ):
            num = getFullNum(iSymbol - 1, jSymbol - 1)
            partNums.append(num)

        if ( data[iSymbol - 1][jSymbol + 1].isdigit() ):
            num = getFullNum(iSymbol - 1, jSymbol + 1)
            partNums.append(num)

    # same logic but for numbers below the symbol
    if ( data[iSymbol + 1][jSymbol].isdigit() ):       
        if ( data[iSymbol + 1][jSymbol - 1].isdigit() ):
            num = getFullNum(iSymbol + 1, jSymbol - 1)
            partNums.append(num)  
        elif ( data[iSymbol + 1][jSymbol + 1].isdigit() ):
            num = getFullNum(iSymbol + 1, jSymbol + 1)
            partNums.append(num)
        else:    
            num = getFullNum(iSymbol + 1, jSymbol)
            partNums.append(num)
    else: 
        if ( data[iSymbol + 1][jSymbol - 1].isdigit() ):
            num = getFullNum(iSymbol + 1, jSymbol - 1)
            partNums.append(num)

        if ( data[iSymbol + 1][jSymbol + 1].isdigit() ):
            num = getFullNum(iSymbol + 1, jSymbol + 1)
            partNums.append(num)

    # lastly, checking left/right of the symbol
    if ( data[iSymbol][jSymbol - 1].isdigit() ):
            num = getFullNum(iSymbol, jSymbol - 1)
            partNums.append(num)

    if ( data[iSymbol][jSymbol + 1].isdigit() ):
            num = getFullNum(iSymbol, jSymbol + 1)
            partNums.append(num)

    return partNums

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

data = [list(line) for line in data]

partNumbers = []

for i in range(len(data)):
    for j in range(len(data[i])): 
        # if we find a symbol
        if (not data[i][j].isdigit() and not data[i][j] == "."):
            # add the part numbers to the list
            partNumbers.extend( getPartNums(i, j) )

sum = 0
for part in partNumbers:
    sum += int(part)

print(sum)
