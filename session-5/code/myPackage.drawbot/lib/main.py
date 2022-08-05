myColCount = 10
myRowCount = 10

Variable([
    dict(name='myColCount', ui='Slider'),
    dict(name='myRowCount', ui='Slider'),
    dict(name='isOval', ui='CheckBox'),
    dict(name='myFill', ui='ColorWell'),
    dict(name='myText', ui='EditText')
    ], globals())

print(isOval)

print(myColCount)
myColCount = int(myColCount)
myRowCount = int(myRowCount)

myCellWidth = width()/myColCount
myCellHeight = height()/myRowCount

for myRowNumber in range(myRowCount):
    for myColNumber in range(myColCount):
        fill(myFill)
        if isOval:
            oval(
                myColNumber*myCellWidth,  #x 
                myRowNumber*myCellHeight,  #y
                myCellWidth, # width
                myCellHeight, # height
            )
        else:
            rect(
                myColNumber*myCellWidth,  #x 
                myRowNumber*myCellHeight,  #y
                myCellWidth, # width
                myCellHeight, # height
            )
            
fontSize(100)
fill(1)
text(myText, (100, 100))