# define a sequences
# a list is a sequence of objects
mySequence = ['bananas', 'apples', 'oranges']
# a string is a sequence of characters
#mySequence = 'hello world'
# a range in a sequence of numbers
mySequence = range(2000, 2100)

# print the sequence
print(mySequence)

# loop through the sequence
# in the process we will create a variable myItem that is equal to the current item in the sequence
for myItem in mySequence:
    # print the item
    print('buy some', myItem)
    # make a new page? or not
    #newPage('Letter')
    # make a big font size
    fontSize(100)
    # set the fill color to random
    fill(random(), random(), random())
    # draw the item
    # convert the item to a string in case it isn’t
    text(
        # first give text() the string to write
        str(myItem), 
        # then give text() the (x, y) coordinates as a tuple
        (
            random()*width(),  # x 
            random()*height()  # y
        ) 
    )
