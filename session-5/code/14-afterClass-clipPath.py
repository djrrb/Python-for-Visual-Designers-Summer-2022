myFormattedString = FormattedString('Hi!', fontSize=900, font='Impact', tracking=-40)

myTextPath = BezierPath()
myTextPath.text(myFormattedString)

translate(40, 150)

with savedState():
    shadow(
        (-20, -20),  # x y offset
        20,  # blur amount
        (0, 0, 0, .2) # shadow fill
    )
    # draw the path in black
    fill(0)
    drawPath(myTextPath)
    
# now forget the shadow and draw a bunch of dots that are clipped
with savedState():
    clipPath(myTextPath)

    myShapeCount = 1000
    for myShapeNumber in range(myShapeCount):
        myShapeSize = randint(0, 100)
        fill(random(), random(), random(), random())
        oval(
            randint(0, width())-myShapeSize/2,
            randint(0, height())-myShapeSize/2,
            myShapeSize,
            myShapeSize,
            )