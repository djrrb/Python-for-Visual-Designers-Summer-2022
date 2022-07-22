myRowCount = 10 # how many rows
myColCount = 10 # how many cols
myGridWidth = width()/myColCount # how wide is column? 
myGridHeight = height()/myRowCount # how tall is each row?

myTicker = 0 # keep track of how many shapes i’ve drawn

# run 1 time
# once per script

# loop through each row, creating myRowNumber in the process
for myRowNumber in range(myRowCount):
    # myRowNumber = 0, 1, 2, 3...
    # things at this indent run 10 times, once per row 
    print('start row number', myRowNumber)
    # begin a saved state
    # we are currently at x=0
    # this will allow us to snap back to the lefthand side
    # when we are done drawing the row
    with savedState():
        # things at this indent are now inside the saved state
        # now loop through each column, creating myColNumber in the process
        for myColNumber in range(myColCount):
            #myColNumber = 0, 1, 2, 3...
            # things at this indent runs 100 times, once per column per row
            print('\t\tdraw col number', myColNumber, myTicker)
            # augment myTicker so we keep track of how many shapes we draw
            myTicker += 1
            # set a random fill color
            fill(random(), random(), random())
            # random() will generate a num between 0 and 1
            # if we want a 50/50 split, we can test if it is less than half
            if random() < .5:
                # if so draw a rect to fill the grid
                rect(0, 0, myGridWidth, myGridHeight)
            else:
                # otherwise draw an oval to fill the grid
                oval(0, 0, myGridWidth, myGridHeight)
            # after we draw the shape, we move one column to the right
            # in preparation for drawing the next column
            translate(myGridWidth, 0)
            # at the end of a set of columns our x position will be off the page
        # dendent once to end the column loop  
    # dedent again to exit the saved state and go back to x=0
    # once per row, we will translate up to the next grid item
    translate(0, myGridHeight)
# dedent all the way and we are completely out of the loops
# print our total number of shapes at the end
print('done! total number of shapes:', myTicker)
        
        