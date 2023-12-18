# instead of storing all numbers and taking up space, just track the min and max numbers that would be affected as well as the offset needed to get the correlating num
# if we go through this list and confirm that a number is within the bounds, take the offset
# this way, we only store 3 numbers per conversion set as opposed to an unknown amount based on the range

file = open("data.txt", "r")
data = file.read()
file.close()

# splitting data into arr based on empty lines
data = data.split("\n\n")
data[0] = data[0].strip("seeds: ")

# converts all the seeds into int values
seeds = [int(val) for val in data[0].split(" ")]
conversionMap = {}
minLocation = None

inputQueue = []
outputQueue = []

# uses the rest of the input data to populate the conversion map
for mapData in data[1: len(data)]:
    # splits up the input section (currently split by conversion categories)
    info = mapData.split(":") 
    numData = info[1].split("\n")
    numData = [[int(num) for num in val.split(" ")] for val in numData[1: len(numData)]]
    conversionMap[info[0]] = numData

# populates the inputQueue with seed values
for i in range(0, len(seeds), 2):
    inputQueue.append( (seeds[i], seeds[i]+seeds[i+1]-1) )

# goes through each conversion type to convert all ranges at once (all seedRanges -> all fertilizerRanges)
for key in conversionMap.keys():
    mapData = conversionMap[key]

    while not len(inputQueue) == 0:
        seedBound = inputQueue.pop(0)
        seedMin = seedBound[0]
        seedMax = seedBound[1]

        converted = False
        for bound in mapData:
            offset = bound[0]-bound[1]
            boundMin = bound[1]
            boundMax = boundMin + bound[2] - 1

            # conversion logic available in excalidraw file
            if (seedMin >= boundMin and seedMax <= boundMax): 
                outputQueue.append( (seedMin+offset, seedMax+offset) )
                converted = True
                break # don't need to check the other bounds when 
            
            elif (seedMin >= boundMin and seedMin <= boundMax) and seedMax > boundMax: 
                outputQueue.append( (seedMin+offset, boundMax+offset) )
                inputQueue.append( (boundMax+1, seedMax) ) # unconverted ranges sent into input if it possibly converts
                converted = True
        
            elif seedMin < boundMin and (seedMax >= boundMin and seedMax <= boundMax):
                inputQueue.append( (seedMin, boundMin-1) )
                outputQueue.append( (boundMin+offset, seedMax+offset) )
                converted = True
        
        # if it went through all conversion ranges and didn't convert, send it to the next conversion as is
        if (not converted):
            outputQueue.append( (seedMin, seedMax) )
    
    inputQueue = outputQueue[:]
    outputQueue = []

min = inputQueue[0][0]
for ranges in inputQueue:
    if (ranges[0] < min):
        min = ranges[0]

print(min)
