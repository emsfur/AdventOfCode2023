file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()
sum = 0

numConversion = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

checkArr = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]

for line in data:
    inpLength = len(line)

    numIdx = [inpLength, -1] # set it to farthest from starting point on both sides (one index out of bounds)
    num = [None, None] # store the first/last digit
    

    for check in checkArr:
        firstCheck = line.find(check)
        lastCheck = line.rfind(check)

        # check if there's a digit/string number index more closer to the start (cover for -1 if substring not found)
        if (firstCheck != -1 and firstCheck < numIdx[0]):
            # update the new first number and value
            numIdx[0] = firstCheck

            if (check.isdigit()):
                num[0] = check
            else:
                # account for converting string number to digit
                num[0] = numConversion[check] 

        # check if there's a digit/string number index more closer to the end than current
        if (lastCheck > numIdx[1]):
            numIdx[1] = lastCheck

            if (check.isdigit()):
                num[1] = check
            else:
                num[1] = numConversion[check]

    sum += int(num[0] + num[1])



print(sum)
