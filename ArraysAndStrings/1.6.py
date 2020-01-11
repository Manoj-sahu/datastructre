s = 'aabbbbcdd'

def compresString(s):
    consecCount = 0
    compressedString = ''
    for i in range(len(s)):
        consecCount +=1
        if i+1 >= len(s) or s[i] != s[i+1]:
            compressedString += s[i] + str(consecCount)
            consecCount = 0

    return compressedString
cs = compresString(s)
print(cs)
print(cs  if len(cs) < len(s) else s)

