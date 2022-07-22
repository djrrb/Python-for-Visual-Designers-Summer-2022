# imagePixelColor() is our eyedropper

# call an image
myImage = ImageObject('black-raspberries.jpg')

# make a grid like we did before
myColCount = 20
myRowCount = 20
myColWidth = width()/myColCount
myRowHeight = height()/myRowCount

# loop through the rows
for myRowNumber in range(myRowCount):
    # this code runs once per row
    # myRowNumber = 0, 1, 2, 3...
    # loop through the cols
    for myColNumber in range(myColCount):    
        # this code runs once per column per row
        # myColNumber = 0, 1, 2, 3...
        # calculate our x and y coordinates for any given grid cell
        # by multiplying what column/row we are on by the width/height of each cell
        # (if we are on the fifth column and each one is 100 wide, our x = 500)
        myX = myColNumber * myColWidth
        myY = myRowNumber * myRowHeight
        # let’s keep track of our main variables by printing them
        print(
            'col:', myColNumber, 
            'row:', myRowNumber, 
            'x:', myX, 
            'y:', myY
            )
        # eyedrop the color from our image at (myX, myY)
        myColor = imagePixelColor(myImage, (myX, myY))
        # set the fill to that color
        # using the asterisk to “unpack” the values
        # so r, g, b, a are fed separately: fill(r, g, b, a) 
        # and not as a single tuple: fill((r, g, b, a))
        fill(*myColor)
        # finally draw our shape
        oval(myX, myY, myColWidth, myRowHeight)