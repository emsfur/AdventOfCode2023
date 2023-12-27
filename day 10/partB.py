# was stuck on figuring out how to implement raycasting for with special case of closed pipe spaces in mind
# but got it thanks to the explanation by @HyperNeutrino // https://youtu.be/r3i3XE9H4uw

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

maze = [] # stores all maze (input) data
loopMap = [] # create a matching sized matrix to for tracking pipes in the loop ('.' if irrelevant)
coordQueue = [] # used to store valid paths out (as coords)

# shows valid pipes to leave current pipe
paths = {
    'top': ['7', 'F', '|'],
    'bot': ['J', 'L', '|'],
    'left': ['L', 'F', '-'],
    'right': ['J', '7', '-']
}

# shows valid ways out of the current pipe
dirs = {
    '|': ['top', 'bot'],
    '-': ['right', 'left'],
    'L': ['top', 'right'],
    'J': ['top', 'left'],
    '7': ['bot', 'left'],
    'F': ['bot', 'right'],
    'S': ['left', 'right', 'top', 'bot']
}

# extra long way of seperating lines into individual chars to get 2D matrix
# but doing it anyways to find starting coordinates
for i, line in enumerate(data):
    loopMap.append(['.' for char in line])
    maze.append([char for char in line])

    if ('S' in line):
        # (y, x) just cause it's easier for retrieving data cause maze[y][x]
        coordQueue.append( (i, line.index('S')) )
        # also create starting point as X on distance map
        loopMap[i][line.index('S')] = 'S'

# handle all the work for checking if the path is valid
rangeY = len(maze)
rangeX = len(maze[0])
def validPath(nextCoord, currCoord, dir):
    currY, currX = currCoord
    y, x = nextCoord
    
    # first make sure that the coords are in bounds of the maze
    if not ((y >= 0 and y < rangeY) and (x >= 0 and x < rangeX)):
        return False

    currPipe = maze[currY][currX]
    nextPipe = maze[y][x]

    # make sure it's not ground
    if (currPipe == '.'):
        return False

    # first part checks if the direction is valid for the current pipe
    # second part checks if it's a connected pipe based on travel direction
    # third part makes sure the coord hasn't been explored yet by checking if distance map marked
    return ( (dir in dirs[currPipe]) and (nextPipe in paths[dir]) and loopMap[y][x] == '.')

# while the queue is not empty
while (coordQueue):
    nextCoords = []

    for i in range(len(coordQueue)):
        currCoord = coordQueue.pop(0)
        
        leftCoord, rightCoord = (currCoord[0], currCoord[1] - 1), (currCoord[0], currCoord[1] + 1)
        topCoord, botCoord = (currCoord[0] - 1, currCoord[1]), (currCoord[0] + 1, currCoord[1])

        # if the coord is valid and connects to current pipe, add it to queue and mark the distance map
        if (validPath(leftCoord, currCoord, 'left')):
            nextCoords.append(leftCoord)
            loopMap[leftCoord[0]][leftCoord[1]] = maze[leftCoord[0]][leftCoord[1]]

        if (validPath(rightCoord, currCoord, 'right')):
            nextCoords.append(rightCoord)
            loopMap[rightCoord[0]][rightCoord[1]] = maze[rightCoord[0]][rightCoord[1]]

        if (validPath(topCoord, currCoord, 'top')):
            nextCoords.append(topCoord)
            loopMap[topCoord[0]][topCoord[1]] = maze[topCoord[0]][topCoord[1]]

        if (validPath(botCoord, currCoord, 'bot')):
            nextCoords.append(botCoord)
            loopMap[botCoord[0]][botCoord[1]] = maze[botCoord[0]][botCoord[1]]

    # add on the next coords list to the queue
    coordQueue.extend(nextCoords)

# spaces within the loop when scanning left->right
withinRight = 0 
# spaces within the loop when scanning top->down
withinDown = 0

# scans left to right
for y, row in enumerate(loopMap):
    inside = False
    riding = False
    up = None
    for x, char in enumerate(row):
        if (char == '.'):
            # loopMap[y][x] = 'I' if inside else 'O' # I = in / O = out
            if (inside): withinRight += 1
        elif (char == '|'):
            # when passing through vertical, we know for sure we've cut in/out of the loop
            inside = not inside
        elif (char in ['F', 'L']):
            # we're scanning left to right, so F or L means we're starting to go along edge
            riding = True
            up = (char == 'L')
        elif (char in ['J', '7']):
            # if we have a L7 or FJ (spaces inbetween dont matter)
            # that means we've crossed over the loop rather than
            # riding the edge and leaving it (in the case of LJ or F7)
            if ( (char == '7' and up) or (char == 'J' and not up) ):
                inside = not inside

            riding == False
            up = None # we've left edge so no value for up
        elif (char == '-'):
            # kinda just riding the pipe here so it don't matter
            pass

# scans top to bot
for x in range(rangeX):
    inside = False
    riding = False
    left = None
    for y in range(rangeY):
        char = loopMap[y][x]
        if (char == '.'):
            if (inside): withinDown += 1
        elif (char == '-'):
            # when passing through horizontal, we know for sure we've cut in/out of the loop
            inside = not inside
        elif (char in ['7', 'F']):
            # we're scanning left to right, so 7 or F means we're starting to go down along edge
            riding = True
            left = (char == '7')
        elif (char in ['J', 'L']):
            if ( (char == 'L' and left) or (char == 'J' and not left) ):
                inside = not inside

            riding == False
            left = None # we've past the edge so no value
        elif (char == '|'):
            # kinda just riding the pipe here so it don't matter
            pass
            
# we want the overlap between the two scans so take min between the two
print(min(withinRight, withinDown))