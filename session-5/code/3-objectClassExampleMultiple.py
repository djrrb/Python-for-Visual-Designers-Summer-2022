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
        

# global variables
myFrameCount = 20
myDotCount = 20

# build instances of our objects
# make an empty list that we will fill with objects
myDotList = []
# make a loop
for myDotNumber in range(myDotCount):
    # get a random x and y
    myRandomX = randint(0, width())
    myRandomY = randint(0, height())
    # make a dot instance
    myDot = GrowingDot((myRandomX, myRandomY), (50, 50))
    # add the dot to our list of dots
    myDotList.append(myDot)

print(myDotList)

# now draw our frames and let the objects draw themselves

for myFrameNumber in range(myFrameCount):
    newPage()
    for myDot in myDotList:
        myDot.draw()
        myDot.bumpSize()

saveImage('objectClassExampleMultiple.gif')