# make a list
myList = ['apples', 
    'oranges',
    'bananas',
    'grapefruit'
]

# print its length
print(len(myList))

print ('=========')
# slice some items
print('first item:', myList[0])
print('last item:', myList[-1])
print('first two items:', myList[:2])
print('all items but the first:', myList[1:])
# a slice of a slice
print('first character of last item:', myList[-1][0])
print('last character of first item:', myList[0][-1])

print ('=========')
# loop through each item on the list and test its first character
for myItem in myList:
    # if the first character is o
    if myItem[0] == 'o':
        print('yay!', myItem, 'starts with a o!')
    # otherwise, tell us what the first character is
    else:
        print('boo!', myItem, 'starts with a', myItem[0])

print ('=========')
# drill down into that list with a loop
for myItem in myList:
    # print each item and its length
    print(myItem, len(myItem))
    # now drill down into each character of each item
    for myChar in myItem:
        print('\t', myChar)

