file = open("data.txt", "r")
data = [val.strip("\n") for val in file.readlines()]
file.close()   

data = {entry[0]: int(entry[1]) for entry in (val.split() for val in data)}

typeMap = {"Five of a kind": [], 
         "Four of a kind": [],
         "Full house": [],
         "Three of a kind": [],
         "Two pair": [],
         "One pair": [],
         "High card": []}

# creates a basis for the number and value order of the cards 
cards = 'J23456789TQKA'

def handPlacement(hand):
    # initialize the counter map with zero for each card count
    count = {val: 0 for val in cards}

    # go through the hand and tally up the counts for each card
    for i in range(5):
        card = hand[i]
        count[card] += 1
    
    # get the top 3 values within the map to determine what the hand should be catagorized as 
    maxCard1, maxCard2, maxCard3 = sorted(count, key=count.get, reverse=True)[:3]
    
    # if J is one of the top 2, just combine them together as top value and make the 3rd max card as 2nd max value
    if ('J' in [maxCard1, maxCard2]):
        maxVal1 = count[maxCard1] + count[maxCard2]
        maxVal2 = count[maxCard3]
    else:
        # we know that J wont combine with itself so have it strengthen top card value
        maxVal1 = count[maxCard1] + count['J']
        maxVal2 = count[maxCard2]


    # catagorize the hand and append it to the map accordingly
    if (maxVal1 == 5):
        typeMap["Five of a kind"].append(hand)
    elif (maxVal1 == 4):
        typeMap["Four of a kind"].append(hand)
    elif (maxVal1 == 3 and maxVal2 == 2):
        typeMap["Full house"].append(hand)
    elif (maxVal1 == 3):
        typeMap["Three of a kind"].append(hand)
    elif (maxVal1 == 2 and maxVal2 == 2):
        typeMap["Two pair"].append(hand)
    elif (maxVal1 == 2):
        typeMap["One pair"].append(hand)
    else:
        typeMap["High card"].append(hand)

for hand in data.keys():
    handPlacement(hand)

winnings = 0
rank = 1
# go through each hand from weakest to strongest
for handGroups in reversed(typeMap.values()):
    # for x in handGroup, sort it based on the custom character order given
    handGroups = sorted(handGroups, key=lambda x: [cards.index(c) for c in x])

    # get the correlating winnings for the hand and add it to winning output amount
    for hand in handGroups:
        winnings += data[hand] * rank
        rank += 1


print(winnings)