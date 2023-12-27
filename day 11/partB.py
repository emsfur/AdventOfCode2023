# all the code stays the same except the spaceTimeDist value

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

sumPaths = 0
# add custom gap distance (-1 since it replaces instead of adding on)
# distance algo already accounts for original gap
spaceTimeDist = 999999 

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

# populate the galaxy maps with coords for each galaxy
galaxyCoords = {}
galaxyID = 1
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if (char == '#'):
            galaxyCoords[galaxyID] = (y, x)
            galaxyID += 1

# checks if the gap index is between a and b 
def goesThroughGap(gap, a, b):
    return (b > gap and gap > a) or (a > gap and gap > b)

# since we want unique pairs checked, we'll just go backwards
# through the IDs and connect them to all numbers lower than itself 
# EX: ID 8 paths to IDs 7 - 0
for pointA in range(galaxyID-1, 0, -1):
    aY, aX = galaxyCoords[pointA]
    for pointB in range(pointA-1, 0, -1):
        bY, bX = galaxyCoords[pointB]
        colCrossed, rowCrossed = 0, 0

        # go through each gap and see if we cross that gap
        for col in emptyCols:
            if (goesThroughGap(col, aX, bX)):
                colCrossed += 1
        
        for row in emptyRows:
            if (goesThroughGap(row, aY, bY)):
                rowCrossed += 1

        # just the math for distance between two points (with only up/down/left/right movement)
        # adds on the extra gap at the end based on how many gaps crossed
        path = ( abs((bX - aX))) + ( abs((bY - aY))) + ((rowCrossed + colCrossed) * spaceTimeDist)
        sumPaths += path

print(sumPaths)

# 9418609