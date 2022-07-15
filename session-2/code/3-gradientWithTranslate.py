# draw a gradient but don’t worry about calculating X...just use translate

myShapeCount = 10 # how many shapes

myR = 0 # red
myG = 0 # green
myB = 0 # blue
myW = width()/myShapeCount # width (the full width of the canvas divided by the number of shapes)
myH = height() # the full height of the canvas

# for item in sequence:
for myShape in range(myShapeCount):
    # set our fill color
    fill(myR, myG, myB)
    # set our rectangle at (0, 0)
    # we will never change this since we will move the canvas instead
    rect(0, 0, myW, myH)
    # augment our blue value by increasing it by a little bit
    # determine that little bit by dividing 1 by number of shapes, so that the whole loop amounts to 1
    myB += 1/myShapeCount
    # move our canvas over by the width of the shape
    translate(myW, 0)