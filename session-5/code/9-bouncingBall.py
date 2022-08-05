
myShapeSize = 50
myShapeCount = 20
myFrameCount = myShapeCount


for myFrameNumber in range(myFrameCount):
    newPage()
    # draw from the middle of the canvas
    # don’t translate x, just change myY
    translate(width()/2, height()/2)
    for myShapeNumber in range(myShapeCount):
        if myFrameNumber == myShapeNumber:
            # get the progress 
            myProgress = myShapeNumber / myShapeCount
            mySineValue = sin(myProgress * 2*pi)
            myY = mySineValue * height()/2
            print(myProgress, myY)
            oval(0, myY, myShapeSize, myShapeSize)
        
saveImage('bouncingBall.gif')