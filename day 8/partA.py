file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()  

directions = data[0]
dirLength = len(directions)

# populates graph from data input (since we only have left/right we can assume idx0 = left and idx1 = right)
# EX: { AAA : (BBB, CCC) } means at node AAA, leftPath is BBB and rightPath is CCC 
network = {pathInfo[0]: tuple(pathInfo[1][1:-1].split(", ")) for pathInfo in (node.split(" = ") for node in data[2:])}

numSteps = 0
idx = 0
currNode = 'AAA'

while (not currNode == 'ZZZ'):
    direction = directions[idx]
    
    # set currNode as left/right node based on direction
    currNode = network[currNode][0] if (direction == 'L') else network[currNode][1]

    numSteps += 1
    idx = (idx + 1) % dirLength # allows us to repeat the direction sequence 

print(numSteps)