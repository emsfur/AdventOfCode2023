file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

maze = [] # stores all maze (input) data
distMap = [] # create a matching sized matrix to for tracking distance
coordQueue = [] # used to store valid paths out (as coords)
dist = 1

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
    distMap.append(['.' for char in line])
    maze.append([char for char in line])

    if ('S' in line):
        # (y, x) just cause it's easier for retrieving data cause maze[y][x]
        coordQueue.append( (i, line.index('S')) )
        # also create starting point as 0 on distance map
        distMap[i][line.index('S')] = 0


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
    return ( (dir in dirs[currPipe]) and (nextPipe in paths[dir]) and distMap[y][x] == '.')

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
            distMap[leftCoord[0]][leftCoord[1]] = dist

        if (validPath(rightCoord, currCoord, 'right')):
            nextCoords.append(rightCoord)
            distMap[rightCoord[0]][rightCoord[1]] = dist

        if (validPath(topCoord, currCoord, 'top')):
            nextCoords.append(topCoord)
            distMap[topCoord[0]][topCoord[1]] = dist

        if (validPath(botCoord, currCoord, 'bot')):
            nextCoords.append(botCoord)
            distMap[botCoord[0]][botCoord[1]] = dist

    # add on the next coords list to the queue
    coordQueue.extend(nextCoords)
    dist += 1
    
print(dist-2)
