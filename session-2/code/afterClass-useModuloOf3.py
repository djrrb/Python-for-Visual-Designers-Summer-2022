# set a shape size
myShapeSize = width()

# move to the middle of the canvas
# doesn’t have to be the exact center :-D
translate(width()/3, height()/3)

# loop through our shapes
for myShape in range(50):
    # show the shape number and the modulo 3
    # it will be a cycle of 0 1 2 0 1 2 0 1 2 0 1 2 ...
    print(myShape, myShape % 3)
    # if it’s zero make it black
    if myShape % 3 == 0:
        fill(0)
    # if it’s one, make it red
    # only rotate if it’s red because why not
    elif myShape % 3 == 1:
        fill(1, 0, 0)
        rotate(3)
    # if it’s two, make it white
    # and rotate the other direction
    else:
        fill(1)
        rotate(-3)
    # draw the rectangle from the middle
    # using 1/3 instead of one half for funsies
    rect(-myShapeSize/3, -myShapeSize/3, myShapeSize, myShapeSize)
    # scale each shape by .9
    scale(.9)
        