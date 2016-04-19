# Qn 1: Find Duplicates

def findDuplicate(array):
    numbers = list(set(array))
    for i in numbers:
        array.remove(i)
    print(len(array))
findDuplicate([1,2,3,4,5,5,9,3,5,3,1])
