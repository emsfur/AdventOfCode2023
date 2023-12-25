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

        # works same way as partA, but just followed the math difference from example (insert in at the left)
        upperSeq.insert(0, upperSeq[0] - seq[0])

    return stack[0][0]

sumVals = 0
for dataset in data:
    sumVals += getNextVal(dataset)

print(sumVals)