# define a sequence
mySequence = 'hello world'

# loop through the sequence
# in the process we will create a variable myItem that is equal to the current item in the sequence
for myItem in mySequence:
    # everything indented will run once for each item
    # print the item
    print('gimme an', myItem, '!')
# once we dedent, the code is no longer part of the loop and will run once
print('done')