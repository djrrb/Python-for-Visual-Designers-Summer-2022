myShapeCount = 10
myX = 0
myR = 0
myG = 0
myB = 0
myW = width()/myShapeCount
myH = height()

# for item in sequence:
for myShape in range(myShapeCount):
    print(myShape, myX)
    fill(myR, myG, myB)
    rect(myX, 0, myW, myH)
    myX += myW # myX = myX + 100
    myB += 1/myShapeCount
    #print('blue value', 1/myShapeCount)