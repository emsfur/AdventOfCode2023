file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

maxCube = {"red" : 12, "green": 13, "blue": 14} # track the given number of cubes of each color
sumPossible = 0

for line in data:
    markedImpossible = False
    
    # split up the line data into what segments we want
    line = line.split(": ")
    gameID = int(line[0].strip("Game "))
    for set in line[1].split("; "):
        for pick in set.split(", "):
            pickData = pick.split(" ")
            numCubes = int(pickData[0])
            colorCube = pickData[1]

            # if the number of cubes picked surpasses the possible number of cubes for a color, mark it as impossible
            if (numCubes > maxCube[colorCube] and not markedImpossible):
                markedImpossible = True
                break
        
        # necessary to prevent having unnessessary iterations 
        if (markedImpossible):
            break

    # if it's a valid set of picks, then game id add to the sum
    if (not markedImpossible):
        sumPossible += gameID
            
print(sumPossible)