file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()    

# split the numbers from the game id
data = [line.split(": ")[1] for line in data]

# create a spot for each scratch card with a default multiplier (1)
numCards = [1 for i in range(len(data))]

for i in range(len(data)):
    # isolate the winning numbers and break into an int array
    winningString = data[i].split(" | ")[0]         # range(start, end, incrementVal)
    winNums = [ int(winningString[i:i+3]) for i in range(0, len(winningString), 3) ] 

    # isolate the scratch numbers and do the same
    scratchString = data[i].split(" | ")[1]
    scratchNums = [ int(scratchString[i:i+3]) for i in range(0, len(scratchString), 3) ]

    numMatches = 0
    
    # compare all the winning numbers and see if they're in the scratch numbers to find valid matches
    for num in winNums:
        if (num in scratchNums):
            numMatches += 1

    # increases the number of scratchcards after the current based on number of matches
    for j in range(i, i + numMatches):
        numCards[j+1] += numCards[i] 
        
sum = 0
for num in numCards:
    sum += num

print(sum)
