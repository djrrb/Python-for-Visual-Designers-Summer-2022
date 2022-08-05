
myDict = { 
    'oranges': 2,
    'apples': 4,
    'bananas': 16
    }

print('— get the value for bananas:', myDict['bananas'])

print('— get a list of the dict keys:', list(myDict.keys()))
print('— get a list of the dict values:', list(myDict.values()))

print('— loop through the keys in a dict')
for myKey in myDict:
    print('\t', myKey)
    print('\t\t', 'and get its value:', myDict[myKey])