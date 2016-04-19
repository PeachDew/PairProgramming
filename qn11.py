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
