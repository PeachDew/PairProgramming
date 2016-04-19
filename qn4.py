# Qn 4(a): Highest Lowest

def findHighestLowest(array):
    highest = 0
    lowest = array[0]
    for i in array:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
    print(highest, lowest)

findHighestLowest([1,2,3,4,5,453,6,4,0])


# Qn 4(b): Highest Lowest, Duplicates

def findHighestLowest(array):
    highest = 0
    lowest = array[0]
    for i in array:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
    print(highest, lowest)

findHighestLowest([1,2,3,4,5,453,6,4,0])
