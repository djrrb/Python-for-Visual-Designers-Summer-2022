# move up and to the right a little
translate(200, 200)
 
# define a function that we can use in our script
# it is called triangle()
# and it takes four required arguments: 
# myX, myY, myShapeWidth, myShapeHeight
# these arguments will become variables within our function
def triangle(myX, myY, myShapeWidth, myShapeHeight):
    # save our state so that transformations within the function
    # don’t affect other parts of the script
    with savedState():
        # move to (myX, myY), this is now our starting point
        translate(myX, myY)
        # print if we want
        print('this is a triangle')
        # draw a polygon to create our triangle
        polygon(
            (0, 0), # lower left
            (myShapeWidth/2, myShapeHeight), # middle top
            (myShapeWidth, 0) # lower right
        )
    # dedent exits our saved state
# another dedent exits our function
# now we are in our main script

# now we can use and reuse the triangle function to our heart’s content
triangle(0, 0, 100, 100)
triangle(0, 100, 50, 50)
triangle(50, 100, 50, 50)
translate(300, 300)
triangle(0, 0, 100, 100)
fill(0, 1, 0)
translate(0, -300)
triangle(100, 100, 200, 200)
