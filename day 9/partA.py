file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

data = [[int(val) for val in seq.split()] for seq in data]

def getNextVal(history):
    stack = [history]

    # keeps going through the difference intervals till they're all 0 and adds it to stack
    while(not all(val == 0 for val in stack[-1])):
        historyItr = stack[-1]
        stack.append([ historyItr[i+1] - val for i, val  in enumerate(historyItr[:-1]) ])
    
    # now go through the stack until we're down to only containing original dataset
    while (not len(stack) == 1):
        # goes through the difference intervals trace (starts off as list of 0's on first iter)
        seq = stack.pop()
        upperSeq = stack[-1]

        # adds the *extrapolated* value onto the next interval array (going up the line till we reach orig dataset)
        # extrapolated by taking the last value of the upperSeq and adding the interval pattern to get next value
        upperSeq.append(upperSeq[-1] + seq[-1])

    return stack[0][-1]

sumVals = 0
for dataset in data:
    sumVals += getNextVal(dataset)

print(sumVals)