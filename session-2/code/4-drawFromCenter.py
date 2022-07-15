# set a width for the shape
myW = width()-100

# move our (0, 0) to the center of canvas
translate(width()/2, height()/2)
# draw shape from the center by subtracting half the width and half the height from (0, 0)
oval(-myW/2, -myW/2, myW, myW)
