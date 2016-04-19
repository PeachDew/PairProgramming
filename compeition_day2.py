# Qn 1: Find Duplicates

def findDuplicate(array):
    numbers = list(set(array))
    for i in numbers:
        array.remove(i)
    print(len(array))
findDuplicate([1,2,3,4,5,5,9,3,5,3,1])

# Qn 2: Remove Duplicates

def removeDuplicate(array):
    numbers = list(set(array))
    for i in numbers:
        array.remove(i)
    print(array)
removeDuplicate([1,2,3,4,5,5,9,3,5,3,1])


# Qn 3: Have integer

def haveint(array, integer):
    for i in array:
        try:
            i // 2
            if i == integer:
                return True
        except:
            a = ''
    return False

print(haveint(['a','c','b'], 1))

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


# Qn 4(a): Highest Lowest, Duplicates

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

# Qn 5: 


# Qn 6: Find Unique

array = [1, 1, 2, 2, 3, 9, 4, 4, 5, 5]

nodups = list(set(array))
dups = []
for i in nodups:
    dups.append(i)
    dups.append(i)
for i in array:
    dups.remove(i)

print(dups)

# Qn 7: Find Intersection

def findInters(a, b):
    print(list(set(a) & set(b)))

findInters([1,2,3,5], [1,2,5])


# Qn 8: Find kth smallest.

def kthsmall(array, k):
    karray = [array[0]]
    for i in array:
        if i < karray[0]:
            karray[0] = i
    

# Qn


# Qn 10: Intersection 3

def findInters3(a, b, c):
    print(list(set(a) & set(b) & set(c)))

findInters3([1,2,3], [1,2,3,4], [3,2,1,0])


# Qn 11: First Repeat

def firstrepeat(array):
    count = 0
    while count < len(array) - 1:
        pivot = array[count]
        for i in range(count+1,len(array)):
            if array[i] == pivot:
                return i
        count += 1
print(firstrepeat([10,5,3,4,3,5,6]))

# Qn 12: First Non Repeat

array = [1, 1, 2, 2, 3, 9, 4, 4, 5, 5]

nodups = list(set(array))
dups = []
for i in nodups:
    dups.append(i)
    dups.append(i)
for i in array:
    dups.remove(i)

print(dups[0])

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


