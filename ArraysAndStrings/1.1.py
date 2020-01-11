# find a string is unique or not

s = 'mannojj'
unique = []
for m in s:
    if m not in unique:
        unique.append(m)
    else:
        print('string is not unique')
        break
    if len(unique) == len(s):
        print("string is unique")

#find unique
unique = []
for m in s:
    if m not in unique:
        unique.append(m)
print(unique, '')
print(','.join(unique))

#find the count of chars
unique = {}
for m in s:
    if m not in unique:
        unique[m] = 1
    else:
        unique[m] += 1
print(unique)

#without any data structure find string has unique char or not
s = 'man'
isUnique = True
for index, m in enumerate(s):
    if m in s[index + 1:]:
        print('string doesnt have unique char')
        isUnique = False
        break

if isUnique:
    print('string is unique')

# without any data structure appraoch 2
s = 'qqq'
s = ''.join(sorted(s))
isUnique = True
for i in range(len(s) -1):
    if s[i] == s[i + 1]:
        print('not unique')
        isUnique = False
        break

if isUnique:
    print('unique')



    


    


