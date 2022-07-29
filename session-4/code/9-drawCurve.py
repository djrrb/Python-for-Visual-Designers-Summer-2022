# define an amount of handle wiggle
myWiggle = 300
# define the base height of the shape we are drawing
myBaseHeight = height()/2

# define a shape
myShape = BezierPath()
# start ourselves at (0, 0), the bottom left
myShape.moveTo((0, 0))
# draw a horizontal line across to the bottom right
myShape.lineTo((width(), 0))
# draw a vertical line up to our shape’s height
myShape.lineTo((width(), myBaseHeight))

# the curve will be three points: handle1, handle2, endpoint

# handle 1 goes above the previous point by a random amount
myHandle1 = (
    width(), 
    myBaseHeight+randint(-myWiggle, myWiggle)
)
# handle 2 is back on the left side of the page, and its y is also the shape height a wiggle amount
myHandle2 = (
    0, 
    myBaseHeight+randint(-myWiggle, myWiggle)
)
# the endpoint is on the left of the page at the basic shape height,
# directly across from the end of the prevous line
myCurveEndpoint = (0, myBaseHeight)

# now draw the curve
myShape.curveTo(
    myHandle1, # handle 1
    myHandle2, # handle 2
    myCurveEndpoint # endpoint
    )

# draw the path to canvas
drawPath(myShape)

# can also draw the handles as well to visualize them
myHandleSize = 100
# set red fill
fill(1, 0, 0)
# draw an oval for each handle, centering the oval on the handle X and Y
oval(myHandle1[0]-myHandleSize/2, myHandle1[1]-myHandleSize/2, myHandleSize, myHandleSize)
oval(myHandle2[0]-myHandleSize/2, myHandle2[1]-myHandleSize/2, myHandleSize, myHandleSize)
