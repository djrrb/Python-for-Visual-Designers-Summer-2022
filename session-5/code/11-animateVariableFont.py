# Released by DJR under the BSD license 
def lerp(start, stop, amt):
	"""
	Return the interpolation factor (between 0 and 1) of a VALUE between START and STOP.
	https://processing.org/reference/lerp_.html
	"""
	return float(amt-start) / float(stop-start)
	
def norm(value, start, stop):
	"""
	Interpolate using a value between 0 and 1
	See also: https://processing.org/reference/norm_.html
	"""
	return start + (stop-start) * value

def remap(value, start1, stop1, start2, stop2, withinBounds=False):
    """
    Re-maps a number from one range to another.
    """
    factor = lerp(start1, stop1, value)
    if withinBounds:
        if factor < 0: factor = 0
        if factor > 1: factor = 1
    return norm(factor, start2, stop2)


myShapeSize = 50
myShapeCount = 20
myFrameCount = myShapeCount

# do we want to save individual frames as separate images for easy import into AfterEffects?
saveIndividualFrames = False

# loop through the frames
for myFrameNumber in range(myFrameCount):
    if saveIndividualFrames:
        newDrawing()
    newPage()
    # draw a background
    fill(0)
    rect(0, 0, width(), height())
    
    
    # set the font and font size
    font('CondorVariable-VF.ttf')
    fontSize(100)
    
    # get the list of font axes
    myAxes = listFontVariations()
    # get the width min and max
    myWdthMin = myAxes['wdth']['minValue']
    myWdthMax = myAxes['wdth']['maxValue']
    # and the same for italic
    myItalMin = myAxes['ital']['minValue']
    myItalMax = myAxes['ital']['maxValue']
    # and weight
    myWghtMin = myAxes['wght']['minValue']
    myWghtMax = myAxes['wght']['maxValue']
    
    # move to the vertical center    
    translate(0, height()/2)
    for myShapeNumber in range(myShapeCount):
        if myFrameNumber == myShapeNumber:
            # if we are on the frame
            # get the progress through the animation
            myProgress = myShapeNumber / myShapeCount
            
            # get a sine and cosine value
            mySineValue = sin(myProgress * 2 * pi)
            myCosValue = cos(myProgress * 2 *pi)
            
            # use the remap() function to map the sin/cos value (between -1 to 1) to the axis values for the font
            myItalValue = remap(myCosValue, -1, 1, myItalMin, myItalMax)
            myWidthValue = remap(mySineValue, -1, 1, myWdthMin, myWdthMax)
            myWghtValue = remap(myCosValue, -1, 1, myWghtMin, myWghtMax)
            # set the font variations for the canvas
            fontVariations(
                wdth=myWidthValue, 
                ital=myItalValue, 
                wght=myWghtValue
            )
            # draw the text
            fill(1)
            text('hello world', (width()/2, 0), align="center")
            # also draw an oval if we  want
            fill(.1)
            myY = mySineValue * height()/2
            oval(0, myY, myShapeSize, myShapeSize)
    # if we want to save individual frames as images, indent saveImage so it happens once per frame
    if saveIndividualFrames:
        saveImage('varFont_'+str(myFrameNumber)+'.png')

# if we are saving the whole animation
if not saveIndividualFrames:
    saveImage('animateVariableFont.gif')