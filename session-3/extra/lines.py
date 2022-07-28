myPageCount = 30
myMargin = width()/15
myMarginWidth = width()-myMargin*2
myMarginHeight = height()-myMargin*2

for myPageNumber in range(myPageCount):
    newPage()
    rect(0, 0, width(), height())
    stroke(1)
    translate(myMargin, myMargin)
    for i in range(500):
        myX1 = randint(0, int(myMarginWidth))
        myX2 = randint(0, int(myMarginWidth))
        myY1 = randint(0, int(myMarginHeight))
        myY2 = randint(0, int(myMarginHeight))

        line((myX1, myY1), (myX2, myY2))
        
saveImage('lines.gif')