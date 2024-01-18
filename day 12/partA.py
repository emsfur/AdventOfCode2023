import math

file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close() 

def getValidCombos(str, record):
    if '?' not in str:
        if [len(damaged) for damaged in list(filter(None, str.split('.')))] == record:
            return 1
        else:
            return 0

    idx = str.find('?')
    return getValidCombos(str[:idx] + '#' + str[idx + 1:], record) + getValidCombos(str[:idx] + '.' + str[idx + 1:], record)
    

data = [ [ info[0] , [int(val) for val in info[1].split(',')] ]  # converts engineer's records into an int list
        for info in (line.split() for line in data) ]

# sum = 0
# for damagedRecord, record in data:
#     sum += getValidCombos(damagedRecord, record)

# print(sum)

damagedRecord = '?###????????'
record = [3,2,1]
print(getValidCombos(damagedRecord, record))