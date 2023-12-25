import math

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()  

directions = data[0]
dirLength = len(directions)

# populates graph from data input (since we only have left/right we can assume idx0 = left and idx1 = right)
# EX: { AAA : (BBB, CCC) } means at node AAA, leftPath is BBB and rightPath is CCC 
network = {pathInfo[0]: tuple(pathInfo[1][1:-1].split(", ")) for pathInfo in (node.split(" = ") for node in data[2:])}

# returns the number of steps it takes for a path
def getSteps(startingNode):
    numSteps = 0
    idx = 0
    currNode = startingNode

    # continue until the node has a Z in it (checked, all instances of Z are at the end of the Node ID)
    while ('Z' not in currNode):
        direction = directions[idx]
        
        # set currNode as left/right node based on direction
        currNode = network[currNode][0] if (direction == 'L') else network[currNode][1]

        numSteps += 1
        idx = (idx + 1) % dirLength # allows us to repeat the direction sequence continuously 
    
    return numSteps

# gets all starting nodes (node contains A)
currNodes = [node for node in network.keys() if 'A' in node] 

# stores the number of steps needed to reach the destination from all starting paths (independently) 
numSteps = [getSteps(node) for node in currNodes]

# since we know when each path reaches a destination we know that they'll 
# all hit the destination at the same time at a common denominator/multiple (we want LCM)
# EX: if path A reaches destination in 2 steps and path B reaches in 3 steps, they both stop at destination in 6 steps
stepsLCM = math.lcm(*numSteps)
print(stepsLCM)