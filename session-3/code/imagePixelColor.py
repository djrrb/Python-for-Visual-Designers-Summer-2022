# imagePixelColor()
myImage = ImageObject('black-raspberries.jpg')

#image(myImage, (0, 0))

myColCount = 20
myRowCount = 20
myColWidth = width()/myColCount
myRowHeight = height()/myRowCount

for myRowNumber in range(myRowCount):
    for myColNumber in range(myColCount):
        print(myRowNumber, myColNumber)
        myX = myColNumber * myColWidth
        myY = myRowNumber * myRowHeight
        print('myX is', myX)
        myColor = imagePixelColor(myImage, (myX, myY))
        fill(*myColor)

        oval(myX, myY, myColWidth, myRowHeight)
