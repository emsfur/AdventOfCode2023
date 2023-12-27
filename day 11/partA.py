file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

sumPaths = 0

# first manage the expansion by counting blank rows/cols
emptyRows = []
emptyCols = []

for i, row in enumerate(data):
    # just checks if we have # in the row or not
    if '#' not in row: 
        emptyRows.append(i)

# for simplification, zip(*data) just flips the grid sideways
# then just apply the same logic
for i, col in enumerate(zip(*data)):
    if '#' not in col: 
        emptyCols.append(i)

# second part of handling expansion by adding onto data
rowOffset = 0
colOffset = 0

# handles the columns and adds the value for each row
for idx in emptyCols:
    for i in range(len(data)):
        data[i] =  data[i][:idx+colOffset] + '.' + data[i][idx+colOffset:]
    colOffset += 1

# same thing but creates a new row 
for idx in emptyRows:
    data.insert(idx+rowOffset, '.' * len(data[0]))
    rowOffset += 1

galaxyCoords = {}
galaxyID = 1

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if (char == '#'):
            galaxyCoords[galaxyID] = (y, x)
            galaxyID += 1


# since we want unique pairs checked, we'll just go backwards
# through the IDs and connect them to all numbers lower than itself 
# EX: ID 8 paths to IDs 7 - 0
for pointA in range(galaxyID-1, 0, -1):
    aY, aX = galaxyCoords[pointA]
    for pointB in range(pointA-1, 0, -1):
        bY, bX = galaxyCoords[pointB]
        # just the math for distance between two points (with only up/down/left/right movement)
        sumPaths += abs((bX - aX)) + abs((bY - aY)) 

print(sumPaths)
            
