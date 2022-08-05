# set some variables using a UI
Variable([
    dict(name='myColCount', ui='Slider'),
    dict(name='myRowCount', ui='Slider'),
    dict(name='isOval', ui='CheckBox'),
    dict(name='myFill', ui='ColorWell'),
    dict(name='myText', ui='EditText')
    ], globals())

# isOval is a checkbox that will be 0 or 1
print(isOval)

# convert some values to integers if we need to
myColCount = int(myColCount)
myRowCount = int(myRowCount)

# get the width and height of each cell
myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

# draw a grid
for myRowNumber in range(myRowCount):
    for myColNumber in range(myColCount):
        fill(myFill)
        # test to see if we draw an oval
        if isOval:
            oval(
                myColNumber*myCellWidth,  #x 
                myRowNumber*myCellHeight,  #y
                myCellWidth, # width
                myCellHeight, # height
            )
        else:
            rect(
                myColNumber*myCellWidth,  #x 
                myRowNumber*myCellHeight,  #y
                myCellWidth, # width
                myCellHeight, # height
            )
            
# set some text too
fontSize(100)
fill(1)
text(myText, (100, 100))