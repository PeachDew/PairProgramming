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
