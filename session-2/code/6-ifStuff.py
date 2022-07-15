# define a string
myString = 'apples'
# print equivalence
print(myString == 'apples')
# test equivalence
if myString == 'apples':
    print('Yes!')
# test non-equivalence
myString = 'apples'
if myString != 'bananas':
    print('No!')
# test greater than / less than
myNum = -3
if myNum > 1:
    print('greater than one')
# set a toggle
toggle = True
# test the toggle’s truthiness
if toggle:
    print('the toggle is true')
else:
    print('the toggle is false')

# a more complex example testing list length
myList = ['apples', 'oranges', 'bananas', 'grapefruit']
# if our list is greater than 3 items, we go to the store
if len(myList) > 3:
    print('i gotta go to the store')
# if that’s not true but our list is greater than 2 items, we get a warning to go to the store soon
elif len(myList) > 2:
    print('mmm better go soon to the store')
# if our list is 2 or fewer items, we wait to go to the store
else:
    print('i can probably wait')