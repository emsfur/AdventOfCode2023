file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

# Extract time and distance values into seperate int values (split function handles varying spaces in input)
time_values = [int(val) for val in data[0].split()[1:]] 
distance_values = [int(val) for val in data[1].split()[1:]]

# Combine time and distance values into a combined list
raceInfo = list(zip(time_values, distance_values))

output = 1

# going through each race data entry
for raceTime, raceRecord in raceInfo:
    speed = 0
    winPossibilities = 0

    # go up in charge time 
    for chargeTime in range(raceTime+1):
        # calculate the distance 
        dist = speed * (raceTime-chargeTime) 
        # see if it's a valid value to beat the record
        if (dist > raceRecord):
            winPossibilities += 1
        speed += 1

    output *= winPossibilities

print(output)
