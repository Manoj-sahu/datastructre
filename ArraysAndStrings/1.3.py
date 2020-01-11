inputs = 'Mr John Smith  '

print(inputs.rstrip().replace(' ', '%20'))

spaceCount = 0
for i in inputs:
    if i == ' ':
        spaceCount +=1
print(inputs.replace(' ', '%20', spaceCount//2))
