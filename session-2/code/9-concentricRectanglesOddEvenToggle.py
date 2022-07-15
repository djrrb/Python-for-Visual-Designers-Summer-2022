myShapeCount = 21
mySequence = range(myShapeCount)
myW = width()-100
myScaleValue = .9
myStrokeValue = 5

fill(0, 1, 0)
#stroke(1, 0, 0)
#strokeWidth(myStrokeValue)

translate(width()/2, height()/2)
#oval(-10, -10, 20, 20)

myOddEven = True

for myShape in mySequence:
    if myOddEven:
        fill(0)
        myOddEven = False
    else:
        fill(1, 0, 0)
        myOddEven = True
    rect(-myW/2, -myW/2, myW, myW)
    scale(myScaleValue)
    strokeWidth(myStrokeValue)
    myStrokeValue /= myScaleValue
    #print(myStrokeValue)
    rotate(12)