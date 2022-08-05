myShapeSize = 50
myShapeCount = 20
myFrameCount = myShapeCount
# loop through shapes

for myFrameNumber in range(myFrameCount):
    newPage()
    translate(0, height()/2)
    for myShapeNumber in range(myShapeCount):
        # how far are we through the sequence
        myProgress = myShapeNumber/myShapeCount
        # get our sine of the progress across a full circle (2*pi)
        # this is a value between -1 and 1
        mySineValue = sin(2*pi*myProgress)
        # multiply the height value by the sine value to get a y position
        myY = mySineValue * height()/2
        if myFrameNumber == myShapeNumber:
            fill(0)
            oval(0, myY, myShapeSize, myShapeSize)
        else:
            fill(.9)
            oval(0, myY, myShapeSize, myShapeSize)
        translate(width()/myShapeCount)
        
saveImage('simpleAnimationSine.gif')