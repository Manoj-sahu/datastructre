s1 = 'manoj'
s2 = 'omaja'

#based on the sorting the string, if both strings are permutation of each other than they should have same character and same lenght
def checkPerm(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    return False

print(checkPerm(s1, s2))
#one more approach is possible for this
#this is based on the count the character in each string if it is same then strings are permutation of each other



    


    