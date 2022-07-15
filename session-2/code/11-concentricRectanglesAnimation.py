# we will use the HSV function to convert color types
from colorsys import hsv_to_rgb

myShapeCount = 80 # how many shapes on a page
myW = width() # how big is the first shape
myScaleValue = .95 # how much to scale the canvas by each tmie we draw a shape
myRotateValue = 0 # how much to rotate the canvas (make this bigger every page)
myFrameCount = 45 # how many frames to draw

# run once
for myFrame in range(myFrameCount):
    # run once per page
    
    # on each page, reset the hue / saturation / value
    myHue = 0 # red is at the start of the rainbow
    mySat = 1 # full saturation
    myVal = 1 # full value
    
    # draw a new page
    newPage()
    # set the frame duration as a fraction of a second
    # 1/12 is 12 frames per second
    frameDuration(1/12)
    
    # move to the center of the canvas
    translate(width()/2, height()/2)
    
    # loop through each rectangle
    for myShape in range(myShapeCount):
        # run once per shape per page
        
        # set the fill color
        # test if myShape is odd or even using modulo (% 2)
        if myShape % 2:
            # if it’s odd, use a color
            # convert our HSV to RGB using the imported function
            myRGB = hsv_to_rgb(myHue, mySat, myVal)
            # set the fill to our RGB because that’s what drawbot likes...use * to unpack the tuple into 3 values
            fill(*myRGB)
            # augment the hue so we go across the rainbow
            myHue += .05
        else:
            # if it’s even, use black
            fill(0)
            
        # draw a rectangle from the center
        # subtract half the width and height from (0, 0)
        rect(-myW/2, -myW/2, myW, myW)
        
        # now that we’re at the end of the shape loop
        # scale it down and rotate it so the next one is different!
        scale(myScaleValue)
        rotate(myRotateValue)
        # now we are DEDENTING
    # run once per page
    # augment the rotate value so each page rotates a little more, which makes it animate
    myRotateValue += 360/myFrameCount
# run once
# save the gif
saveImage('concentricRectangles.gif')