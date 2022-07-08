mySequence = range(10) # define a sequence
myNumber = 0 # define a variable as 0
for myItem in mySequence:
    # myItem is equal to the item in the sequence (0, 1, 2, 3, 4, 5)
    # myNumber is equal to the number we are going to augment (0, 5, 10, 15, 20)
    print(myNumber) 
    myNumber += 5 # augment the number by adding 5 to the value it had before
# after the loop is done, myNumber is 50
print('final value:', myNumber)