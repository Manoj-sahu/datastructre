s = 'tact coa'

#program to check any permutation of string is palindrome or not

charsFreq = {}

for i in s:
    if i not in charsFreq:
        charsFreq[i] = 1
    else:
        charsFreq[i] += 1

def CheckMaxOneOdd(charsFreq):
    oddFound = True
    for c in charsFreq:
        print(c)
        if charsFreq[c] % 2 == 1:
            if oddFound:
                offFound = False
                return True
        oddFound = True
    return oddFound
print(CheckMaxOneOdd(charsFreq))

        