# save our state
with savedState():
    # move to the center of the canvas
    translate(width()/2, height()/2)
    # set the fill color within the saved state
    fill(0, 1, 0)
    # draw a rectangle at (0, 0)
    rect(0, 0, 100, 100)
    # draw an oval at (100, 100)
    oval(100, 100, 100, 100)
# now draw that same oval again
# but dedenting the line exits the saved state
# dedenting exists the saved state
# and we are back to the lower left
# and a black fill color
oval(100, 100, 100, 100)