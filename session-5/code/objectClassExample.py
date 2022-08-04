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
        
        
myDot = GrowingDot((500, 500), (100, 100))
print(myDot.myPosition)
print(myDot.mySize)

myDot2 = GrowingDot((200, 200), (50, 50))
print(myDot2.myPosition)
print(myDot2.mySize)

myDotList 

myFrameCount = 10
for myFrameNumber in range(myFrameCount):
    newPage()
    myDot.draw()
    myDot.bumpSize()
    myDot2.draw()
    myDot2.bumpSize()
    
saveImage('myDots.gif')