file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()
sum = 0

for line in data:
    inpLength = len(line)
    firstFound = False
    lastFound = False
    num = [None, None]


    # loop doing a two point search for a number; one from the start and one from the end
    for i in range(inpLength):
        if (not firstFound and line[i].isdigit()):
            num[0] = line[i]
            firstFound = True
        
        if (not lastFound and line[inpLength - i - 1].isdigit()):
            num[1] = line[inpLength-i - 1]
            lastFound = True

        # stop loop if we found both digits
        if (firstFound and lastFound):
            break

    sum += int(num[0] + num[1]) 


print(sum)