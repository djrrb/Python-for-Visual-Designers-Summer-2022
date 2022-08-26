myFs = FormattedString(
    'A', 
    font='GimletSansVariable-Light', 
    fontSize=500,
    stroke=(1, 0, 0),
    fill=None,
    )

myPath = BezierPath()
myPath.text(myFs)
myPath.removeOverlap()

myResult = BezierPath()
myResult.moveTo((0, 0))

text(myFs, (0, 0))

translate(500)
fill(None)
stroke(0, 0, 1)
drawPath(myPath)

myJiggle = 5

for myContour in myPath:
    myResult.moveTo(myContour[0][0])
    for mySegment in myContour:
        for myPoint in mySegment:
            oval(myPoint[0]-5, myPoint[1]-5, 10, 10)
            myXOffset = randint(-myJiggle, myJiggle)
            myYOffset = randint(-myJiggle, myJiggle)
            myResult.lineTo((myPoint[0]+myXOffset, myPoint[1]+myYOffset))
    myResult.closePath()

translate(0, 500)
xx = 0
xy = 1.2
yx = .5
yy = 1.2
x = .5
y = 1
transform((xx, xy, yx, yy, x, y))
drawPath(myResult)