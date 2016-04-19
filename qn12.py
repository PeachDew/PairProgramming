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
