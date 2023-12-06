file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

data = [list(line) for line in data]

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
                    
    directions = { "top": (iSymbol-1, jSymbol),      # up direction
                   "bot": (iSymbol+1, jSymbol),      # down direction
                   "left": (iSymbol, jSymbol-1),      # left direction
                   "right": (iSymbol, jSymbol+1),      # right direction
                   "top-left": (iSymbol-1, jSymbol-1),    # top left
                   "top-right": (iSymbol-1, jSymbol+1),    # top right
                   "bot-left": (iSymbol+1, jSymbol-1),    # bottom left
                   "bot-right": (iSymbol+1, jSymbol+1)     # bottom right
                 }

    for d in directions.keys():
        i = directions[d][0]
        j = directions[d][1]

        if (data[i][j].isdigit() ):
            num = getFullNum(i, j)
            directions[d] = num


        print(directions)
    return list( set(partNums) )





partNumbers = []

for i in range(len(data)):
    for j in range(len(data[i])): 
        # if we find a symbol
        if (not data[i][j].isdigit() and not data[i][j] == "."):
            # print("Parts found for symbol " + data[i][j])
            # print("\t" + str(getPartNums(i,j)))

            partNumbers.extend( getPartNums(i, j) )

output = ""
sum = 0
for part in partNumbers:
    sum += int(part)

# print(partNumbers)
print(sum)
# sum = 0
# for numb in partNumbers:
#     sum += int(numb)

# print(sum)

# 534695 TOO LOW


# for line in schematic:
#     print(len(line))


# for line in data:
    # schemLine = []
    # info = ''

    # for char in line:
    #     if (char == '.'):
    #         for i in range(len(info)):
    #             schemLine.append(info)
            
    #         info = ''
    #         schemLine.append(".")

    #     else:
    #         info += char
        

    
    # schematic.append(schemLine)
