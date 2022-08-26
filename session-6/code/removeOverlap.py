# make a formatted string
myFs = FormattedString(
    'A', 
    font='GimletSansVariable-Light', 
    fontSize=500,
    stroke=(1, 0, 0),
    fill=None,
    )

# draw the text as red text     
text(myFs, (0, 0))

# make an empty path
myPath = BezierPath()
# add the text to convert to outlines
myPath.text(myFs)
# remove overlap on the outline
myPath.removeOverlap()

# make a second empty path to store a modified version
myResult = BezierPath()

# move to the right
translate(500)

# draw the path itself in blue
fill(None)
stroke(0, 0, 1)
drawPath(myPath)

# set a jiggle amount
myJiggle = 5

# loop through the contours
for myContour in myPath:
    # move to the first point in the contour
    myResult.moveTo(myContour[0][0])
    # loop throug the segment
    for mySegment in myContour:
        # loop through each point
        for myPoint in mySegment:
            # draw an oval around each point
            oval(myPoint[0]-5, myPoint[1]-5, 10, 10)
            # calculate some random offsets
            myXOffset = randint(-myJiggle, myJiggle)
            myYOffset = randint(-myJiggle, myJiggle)
            # add the point to myResult but with some random jiggle appled
            myResult.lineTo((myPoint[0]+myXOffset, myPoint[1]+myYOffset))
    # close the path at the end of the contour 
    myResult.closePath()

# move up and make pink
translate(0, 500)
stroke(1, 0, 1)
# draw the modified path
drawPath(myResult)