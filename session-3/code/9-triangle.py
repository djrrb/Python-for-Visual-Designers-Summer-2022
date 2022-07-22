# move up and to the right a little
translate(200, 200)
# determine the shape width and height
myShapeWidth = 100
myShapeHeight = 100
# draw a polygon
polygon(
    (0, 0), # start at lower left
    (myShapeWidth/2, myShapeHeight), # move to middle top
    (myShapeWidth, 0) # move to bottom right
    )
    
