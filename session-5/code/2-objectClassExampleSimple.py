# define a new object type
# this will hold information

class GrowingDot():
    # the object can contain methods (functions) and attributes
    
    # the __init__ method will run whenever a new instance
    # of this object type is created
    # we will feed it two arguments
    # in addition to the first argument: the object itself
    def __init__(self, myPosition, myStartSize):
        # store those arguments as attributes
        # that we can access as a part of the object
        self.myPosition = myPosition
        self.mySize = myStartSize

    # here's a method for the object to draw itself  
    def draw(self):
        # draw from the center by subtracting half the width/height
        oval(
            self.myPosition[0]-self.mySize[0]/2,
            self.myPosition[1]-self.mySize[1]/2,
            self.mySize[0],
            self.mySize[1]
            )
    # here’s a method that increases the size attribute
    # randomly by a certain amount
    # we have to do x and y separately
    def bumpSize(self, myMaxAmount=100):
        myW, myH = self.mySize
        myIncrease = randint(0, myMaxAmount)
        self.mySize = myW + myIncrease, myH + myIncrease
        
# create an instance at a certain position and size
myDot = GrowingDot((500, 500), (100, 100))
# get the attributes
print(myDot.myPosition)
print(myDot.mySize)

# do it again, each instance
myDot2 = GrowingDot((200, 200), (50, 50))
print(myDot2.myPosition)
print(myDot2.mySize)

# make a simple animation
myFrameCount = 10
# loop through frames
for myFrameNumber in range(myFrameCount):
    newPage()
    # draw our dots and bump up their sizes
    myDot.draw()
    myDot.bumpSize()
    myDot2.draw()
    myDot2.bumpSize()
    
saveImage('objectClassExample.gif')