# Qn 13: Top two.

def findHighest2(array):
    highest = 0
    second = 0
    for i in array:
        if i > highest:
            highest = i
        else:
            if i > second:
                second = i
    print(highest, second)

findHighest2([1,2,3,4,5,453,453,4,0])
