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

# uses the rest of the input data to populate the conversion map
for mapData in data[1: len(data)]:
    # splits up the input section (currently split by conversion categories)
    info = mapData.split(":") 
    numData = info[1].split("\n")
    numData = [[int(num) for num in val.split(" ")] for val in numData[1: len(numData)]]
    # creates a map containing all conversion ranges tied to conversion type
    conversionMap[info[0]] = numData

def convert(key, val):
    mapData = conversionMap[key]
    # go through all conversion ranges based on key and return converted value
    for bound in mapData:
        if (val >= bound[1] and val < bound[1] + bound[2]):
            return val + (bound[0] - bound[1])
    # return same output value if not in any conversion ranges
    return val

# go through each seed individually
for seed in seeds:
    # use as variable that goes through each conversion one by one
    output = seed
    for key in conversionMap.keys():
        output = convert(key, output) # convert to next type

    # update the min location if found or set as min on first iteration
    if (minLocation == None or output < minLocation):
        minLocation = output

print(minLocation)
