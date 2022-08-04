
# define the object type
class GrowingDot():
    def __init__(self, myPosition, myStartSize):
        self.myPosition = myPosition
        self.mySize = myStartSize
        print('this is a new object!')
    
    def draw(self):
        oval(
            self.myPosition[0]-self.mySize[0]/2,
            self.myPosition[1]-self.mySize[1]/2,
            self.mySize[0],
            self.mySize[1]
            )
        
    def bumpSize(self):
        myW, myH = self.mySize
        myIncrease = randint(0, 100)
        self.mySize = myW + myIncrease, myH + myIncrease
        
# global variable
myFrameCount = 20
myDotCount = 20

# build instances of our objects
myDotList = []
for myDotNumber in range(myDotCount):
    myRandomX = randint(0, width())
    myRandomY = randint(0, height())
    myDot = GrowingDot((myRandomX, myRandomY), (50, 25))
    myDotList.append(myDot)

print(myDotList)

# drawing our frames and letting the objects draw themselves

for myFrameNumber in range(myFrameCount):
    newPage()
    for myDot in myDotList:
        myDot.draw()
        myDot.bumpSize()

saveImage('myDots.gif')