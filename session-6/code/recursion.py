def drawBranch(myBranchLength=100, myDepth=0):
    line((0, 0), (0, myBranchLength))
    if myDepth < 9:
        translate(0, myBranchLength)
        for myDirection in [-1, 1]:
            with savedState():
                rotate(10*myDirection+randint(-10, 10))
                scale(.95)
                drawBranch(myBranchLength, myDepth+1)

stroke(0)
strokeWidth(2)
translate(width()/2, 100)
lineCap('round')
drawBranch(100)