myString = 'hello world'
myList = ['apples', 'oranges', 'bananas']


myDict = { 
    'oranges': 2,
    'apples': 4,
    'bananas': 16
    }

#print(myList[-1])

print(myDict['bananas'])

print(list(myDict.values()))

for myKey in myDict:
    print(myKey, myDict[myKey])