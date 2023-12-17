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
counter = 0
max = 0

# uses the rest of the input data to populate the conversion map
for mapData in data[1: len(data)]:
    # splits up the input section (currently split by conversion categories)
    info = mapData.split(":") 
    numData = info[1].split("\n")
    numData = [[int(num) for num in val.split(" ")] for val in numData[1: len(numData)]]
    conversionMap[info[0]] = numData

def convert(key, val):
    mapData = conversionMap[key]

    for bound in mapData:
        if (val >= bound[1] and val < bound[1] + bound[2]):
            return val + (bound[0] - bound[1])
    return val

def getLocation(seed):
    output = seed
    for key in conversionMap.keys():
            output = convert(key, output)
    
    return output

for i in range(0, len(seeds), 2):
    max += seeds[i+1]


for i in range(0, len(seeds), 2):
    output = ""
    for j in range(seeds[i], seeds[i] + seeds[i+1]):
        output = getLocation(j)

        if (minLocation == None or output < minLocation):
            minLocation = output

        counter += 1
        print(str((counter/max) * 100)  + "%")

    


print(minLocation)


# issue right now is that it goes through all the numbers within the range 