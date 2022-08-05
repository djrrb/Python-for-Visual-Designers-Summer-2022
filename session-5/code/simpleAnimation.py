myShapeSize = 50
myShapeCount = 20
myFrameCount = myShapeCount
for myFrameNumber in range(myFrameCount):
    newPage()
    for myShapeNumber in range(myShapeCount):
        if myFrameNumber == myShapeNumber:
            oval(0, 0, myShapeSize, myShapeSize)
        translate(width()/myShapeCount)
        
saveImage('dotAcrossPage.gif')