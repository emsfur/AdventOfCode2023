file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

# split the numbers from the game id
data = [line.split(": ")[1] for line in data]
pointSum = 0

for line in data:
    # isolate the winning numbers and break into an int array
    winningString = line.split(" | ")[0]         # range(start, end, incrementVal)
    winNums = [ int(winningString[i:i+3]) for i in range(0, len(winningString), 3) ] 

    # isolate the scratch numbers and do the same
    scratchString = line.split(" | ")[1]
    scratchNums = [ int(scratchString[i:i+3]) for i in range(0, len(scratchString), 3) ]
    
    pts = 0
    
    # compare all the winning numbers and see if they're in the scratch numbers
    for num in winNums:
        if (num in scratchNums):
            # for the first match, increase by one
            if (pts == 0):
                pts = 1
                continue
            # double total points for any matches after the first 
            pts *= 2

    pointSum += pts

print(pointSum)


