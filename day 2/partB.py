file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

sumPower = 0

for line in data:
    min = {"red" : 0, "green": 0, "blue": 0} 
    power = 1
    
    # split up the line data into what segments we want
    line = line.split(": ")
    gameID = int(line[0].strip("Game "))
    for set in line[1].split("; "):
        for pick in set.split(", "):
            pickData = pick.split(" ")
            numCubes = int(pickData[0])
            colorCube = pickData[1]

            # if we hit a new minimum required, update it
            if (numCubes > min[colorCube]):
                min[colorCube] = numCubes
        
    # multiply all color minimums for the power value
    for num in min.values():
         power *= num

    # add power value to sum
    sumPower += power
    
            
print(sumPower)