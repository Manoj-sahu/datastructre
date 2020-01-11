#program to find two strings are one character away or not
s1 = 'pale'
s2 = 'bake'

def checkOneAway(s1, s2):
    if len(s1) == len(s2):
        print(onEditReplace(s1, s2))
    elif len(s1) + 1 == len(s2):
        print(onRemoveReplace(s1,s2))
    elif len(s1) -1 == len(s2):
        print(onRemoveReplace(s1, s2))

def onEditReplace(s1, s2):
    onDiffFound = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if(onDiffFound):
                #here it's comes mean there is second diff also
                return False
            onDiffFound = True
    return onDiffFound

def onRemoveReplace(s1, s2):
    i1 = 0
    i2 = 0
    while i2 < len(s2) and i1 < len(s1):
        if s1[i1] != s2[i2]:
            if i1 != i2:
                return False
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True
        

checkOneAway(s1, s2)