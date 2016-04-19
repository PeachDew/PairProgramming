# Qn 8: Find kth smallest.

def kthsmall(array, k):
    karray = [array[0]]
    for i in array:
        if i < karray[0]:
            karray[0] = i
