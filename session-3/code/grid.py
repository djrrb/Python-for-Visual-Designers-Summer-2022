newPage()

myRowCount = 10
myColCount = 10
myGridWidth = width()/myColCount # make this relative to canvas later?
myGridHeight = height()/myRowCount# make this relative to canvas later?

myTicker = 0
# run 1 time
for myRowNumber in range(myRowCount):
    # run 10 times
    print('start row number', myRowNumber)
    # i'm at (0, 0)
    with savedState():
        for myColNumber in range(myColCount):
            # run 100 times
            print('\t\tdraw col number', myColNumber, myTicker)
            myTicker += 1
            fill(random(), random(), random())
            if random() < .5:
                rect(0, 0, myGridWidth, myGridHeight)
            else:
                oval(0, 0, myGridWidth, myGridHeight)
            translate(myGridWidth, 0)
            # i'm at (100, 0), (200, 0)
        # i'm at (0, 0) again 
        # once per col
    # once per row
    translate(0, myGridHeight)
print('done! total number of shapes:', myTicker)
        
        