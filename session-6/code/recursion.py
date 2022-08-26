# a function that draws a line / branch, then rotates and calls on itself
def drawBranch(myBranchLength=100, myDepth=0):
    # draw a vertical line
    line((0, 0), (0, myBranchLength))
    # only keep running a certain depth
    if myDepth < 5:
        # move to the top of the branch
        translate(0, myBranchLength)
        # draw two branches rotating from he start
        # angles are negative and positive
        for myDirection in [-1, 1]:
            # save the state so we snap back to the previous curve
            with savedState():
                # rotate a certin amount plus jiggle
                rotate(25*myDirection+randint(-10, 10))
                # make each level a little smaller
                scale(.95)
                # draw a new branch, incrementing the depth
                drawBranch(myBranchLength, myDepth+1)

# now draw the tree turnk and the other swill follow
stroke(0)
strokeWidth(2)
# move to the middle and with a little bottom borderom
translate(width()/2, 100)
# set the line endings to round
lineCap('round')
# now run the recursive function
drawBranch(100)