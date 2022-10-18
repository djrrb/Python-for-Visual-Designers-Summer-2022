from random import choice

#####
# Some stock functions for interpolation
#####
def norm(value, start, stop):
    """
    Return the interpolation factor (between 0 and 1) of a `value` between `start` and `stop`.
    """
    return (value - start) / (stop - start)


def lerp(start, stop, factor):
    """
    Return an interpolated value between `start` and `stop` using interpolation factor `factor`.
    """
    return start + (stop - start) * factor


def remap(value, start1, stop1, start2, stop2, clamp=False):
    """
    Re-maps a number from one range to another.
    """
    factor = norm(value, start1, stop1)
    if clamp:
        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1
    return lerp(start2, stop2, factor)

### the slice drawing function!

def drawSlice(
    x, y, w, h, # the rectangle 
    offset=(0, 0) # the x, y offset
    # 0, 0 = southwest
    # -1, 0 = southeast
    # -1, -1 = 
):
    """ the simplest execution of a slice drawing """
    with savedState():
        myPath = BezierPath()
        myPath.rect(x, y, w, h)
        clipPath(myPath)
        offsetX, offsetY = offset
        oval(x+offsetX*w, y+offsetY*h, w*2, h*2)
        
        
# our animated slice class
class AnimatedSlice():
    """ A more complex slice that can remember things about itself like where it is and where it is going """
    def __init__(self, x, y, w, h, startOffset):
        # the basic info we need to draw a slice
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.offsetX = startOffset[0]
        self.offsetY = startOffset[1]

        # additional info we need to do an animation
        self.isAnimating = False
        self.currentFrame = None
        self.frameCount = None
        self.startOffsetX = startOffset[0]
        self.startOffsetY = startOffset[1]
        self.endOffsetX = None
        self.endOffsetY = None
        self.restAfter = None
        self.rest = None
        
    def draw(self):
        self.bumpAnimation()
        drawSlice(self.x, self.y, self.w, self.h, (self.offsetX, self.offsetY))
        
    def bumpAnimation(self):
        """run this when we draw a frame to move the animation forward"""
        if self.frameCount:
            # how far are we through the animation?
            phaseProgress = self.currentFrame / (self.frameCount-1)
            # get the new current offset by interpolating between the start and endpoints
            midOffsetX = lerp(self.startOffsetX, self.endOffsetX, phaseProgress)
            midOffsetY = lerp(self.startOffsetY, self.endOffsetY, phaseProgress)
            # bump the frame
            self.currentFrame += 1
            # set the current xy and y offset
            self.offsetX = midOffsetX
            self.offsetY = midOffsetY
            
            # if we have reached the end of our animation, reset our animation variables
            if phaseProgress == 1:
                self.frameCount = None
                self.currentFrame = None
                self.endOffsetX = None
                self.endOffsetY = None
                self.startOffsetX = self.offsetX
                self.startOffsetY = self.offsetY
                if self.restAfter:
                    self.rest = self.restAfter
                    self.restAfter = None
                else:
                    self.isAnimating = False
        if self.rest: 
            self.rest -= 1
            if self.rest == 0:
                self.isAnimating = False
                self.rest = None
                
        
    def animateTo(self, endOffset, frameCount, restAfter=0):
        """begin an animation over a certain number of frames"""
        self.isAnimating = True
        self.startOffsetX = self.offsetX
        self.startOffsetY = self.offsetY
        self.endOffsetX = endOffset[0]
        self.endOffsetY = endOffset[1]
        self.frameCount = frameCount
        self.currentFrame = 0
        self.restAfter = restAfter
        
    # Some canned animations
        
    def shiftRight(self, frames, restAfter=0):
        if self.offsetX <= 0:
            endOffsetX = self.offsetX + 1
            endOffsetY = self.offsetY
            self.animateTo((endOffsetX, endOffsetY), frames, restAfter)
        
    def shiftLeft(self, frames, restAfter=0):
        if self.offsetX >= 0:
            endOffsetX = self.offsetX - 1
            endOffsetY = self.offsetY
            self.animateTo((endOffsetX, endOffsetY), frames, restAfter)
        
    def shiftUp(self, frames, restAfter=0):
        if self.offsetY <= 0:
            endOffsetX = self.offsetX 
            endOffsetY = self.offsetY + 1
            self.animateTo((endOffsetX, endOffsetY), frames, restAfter)
        
    def shiftDown(self, frames, restAfter=0):
        if self.offsetY != -1:
            endOffsetX = self.offsetX 
            endOffsetY = self.offsetY - 1
            self.animateTo((endOffsetX, endOffsetY), frames, restAfter)
            
    def shiftRandom(self, frames, restAfter=0):
        offsetX = choice([0, -1])
        offsetY = choice([0, -1])
        self.animateTo((offsetX, offsetY), frames, restAfter)
            

##### set some global variables

frames = 20
phase = 5
rowCount = 10
colCount = 10
myGridX = width()/colCount
myGridY = height()/rowCount
fps = 1/12
returnToInitalConfiguration = True # do we want the animation to loop easily?


#### initiate the objects with a random offset

# keep a separate list with the initial configuration so we can go back there
# for easy looping
initialConfiguration = []

# rows is a list of rows, each row is a list of shapes
rows = []
for rowNumber in range(rowCount):
    row = []
    for colNumber in range(colCount):
        # get the grid x and y offsets
        x = colNumber * myGridX
        y = rowNumber * myGridY
        # rnandomize the offset
        xOffset = choice([-1, 0])
        yOffset = choice([-1, 0])
        #
        initialConfiguration.append((xOffset, yOffset))
        mySlice = AnimatedSlice(x, y, myGridX, myGridY, (xOffset, yOffset))
        row.append(mySlice)
    rows.append(row)
    
# now draw the objects over the frames
for frame in range(frames):
    newPage()
    frameDuration(fps)
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    for ri, row in enumerate(rows):
        for ci, shape in enumerate(row):
            # begin an animation if the following is true:
            # we are beginning a new phase
            # an animation isn’t currently processing
            # flip a coin
        
            print(frame % phase, frame % phase*2, frame % phase*3, frame % phase*4)
            if ri % 2 and frame % phase == 0:
                shape.shiftRandom(phase, phase)
            elif not ri % 2 and frame % phase*2 == 0:
                shape.shiftRandom(phase, phase)
            elif ci % 2 and frame % phase*3 == 0:
                shape.shiftRandom(phase, phase)
            elif not ci % 2 and frame % phase*4 == 0:
                shape.shiftRandom(phase, phase)
            shape.draw()
          
# this is a little extra section that will return the animation to its initial configuration
# this is helpful if we are looping the animation since there won’t be an abrupt change
# it adds one extra phase to the animation
           
if returnToInitalConfiguration:
    # first, set all the objects to animate at once
    count = 0 
    for row in rows:
        for shape in row:
            shape.animateTo(initialConfiguration[count], phase, phase)
            count += 1
        
    # now run the animation
    for frame in range(phase):
        newPage()
        frameDuration(fps)
        fill(1)
        rect(0, 0, width(), height())
        fill(0)
        count = 0
        for row in rows:
            for shape in row:
                shape.draw()

saveImage('animateRow.gif')
    