myShapeSize = 50
myShapeCount = 20
myFrameCount = myShapeCount

# loop for each page
# and then loop for each shape

# if the shapeNumber matches the frameNumber, that’s the one for our animation

for myFrameNumber in range(myFrameCount):
    newPage()
    for myShapeNumber in range(myShapeCount):
        if myFrameNumber == myShapeNumber:
            fill(0)
            oval(0, 0, myShapeSize, myShapeSize)
        else:
            # draw other ovals as light gray
            fill(.9)
            oval(0, 0, myShapeSize, myShapeSize)
        translate(width()/myShapeCount)
        
saveImage('simpleAnimation.gif')