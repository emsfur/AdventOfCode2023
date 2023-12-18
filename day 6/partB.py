# brute force method of solution, probably a math way of doing it but not my strongsuit

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()   

raceTime = int(data[0].split(":")[1].replace(" ", ""))
raceRecord = int(data[1].split(":")[1].replace(" ", ""))

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

print(winPossibilities)