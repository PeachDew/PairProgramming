# Qn 2: Remove Duplicates

def removeDuplicate(array):
    numbers = list(set(array))
    for i in numbers:
        array.remove(i)
    print(array)
removeDuplicate([1,2,3,4,5,5,9,3,5,3,1])
