myFormattedString = FormattedString('Hi!', fontSize=800, font='Impact', align="center")

myTextPath = BezierPath()
myTextPath.text(myFormattedString)

# move to the lower center
translate(width()/2, 200)

# enter a saved state and draw the text with a shadow
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
            randint(-width()/2, width()/2)-myShapeSize/2,
            randint(0, height())-myShapeSize/2,
            myShapeSize,
            myShapeSize,
            )

# exit the saved state to deactivate the clipping mask
# move down a bit
translate(0, -100)
# set some text outside of the clip path
fill(0)
fontSize(20)
text('how’s it going?', (0, 0), align="center")