import math

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

def groupBy(rowInput, splitVar):
    return list(filter(None, rowInput.split(splitVar)))

checksMade = 0
def getValidCombos(str, record):
    if '?' not in str:
        if [len(damaged) for damaged in groupBy(str, '.')] == record:
            return 1
        else:
            return 0

    firstDmg = groupBy(groupBy(str, '.')[0], '?')
    print(firstDmg)
    if (firstDmg and firstDmg[0].count('#') > record[0]):
        return 0

    global checksMade
    checksMade += 1

    idx = str.find('?')
    return getValidCombos(str[:idx] + '#' + str[idx + 1:], record) + getValidCombos(str[:idx] + '.' + str[idx + 1:], record)
    

data = [ [ info[0] , [int(val) for val in info[1].split(',')] ]  # converts engineer's records into an int list
        for info in (line.split() for line in data) ]

sum = 0
for damagedRecord, record in data: 
    # for i in range(4):
    #     damagedRecord += '?' + damagedRecord
    # arrangements = getValidCombos(damagedRecord, record*5)
    arrangements = getValidCombos(damagedRecord, record)

    addedArrangements = getValidCombos( '?' + damagedRecord, record)  if (damagedRecord[-1] in ['.']) else getValidCombos( damagedRecord + '?', record)
    addedArrangements = math.pow( addedArrangements, 4)

    print(int(arrangements * addedArrangements))
    # print(f'Pre: {int(arrangements * addedArrangementsPre)}   {'\t'} Post: {int(arrangements*addedArrangementsPost)}   {'\t'} Ends with dot: {damagedRecord[-1] == '.'}')

    sum += int(arrangements * addedArrangements)
    # sum += arrangements

# print(sum)
# print(checksMade)

# 17613380164860 too low
