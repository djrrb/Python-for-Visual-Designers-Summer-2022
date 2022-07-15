# a very manual way to draw a gradient
# not recommended but it does the trick

# set the fill color
fill(0, 0, 0)
# set the rectangle 100 wide and the height of the canvas
rect(0, 0, 100, height())
# now do it again and again, changing the color slightly and moving the rectangle 100 to the right
fill(0, 0, .1)
rect(100, 0, 100, height())
fill(0, 0, .2)
rect(200, 0, 100, height())
fill(0, 0, .3)
rect(300, 0, 100, height())
fill(0, 0, .4)
rect(400, 0, 100, height())
fill(0, 0, .5)
rect(500, 0, 100, height())
fill(0, 0, .6)
rect(600, 0, 100, height())
fill(0, 0, .7)
rect(700, 0, 100, height())
fill(0, 0, .8)
rect(800, 0, 100, height())
fill(0, 0, .9)
rect(900, 0, 100, height())