translate(200, 200)
myShapeWidth = 100
myShapeHeight = 100

# for myCount in range(100):  
 
def triangle(myX, myY, myShapeWidth, myShapeHeight):
    with savedState():
        translate(myX, myY)
        print('this is a triangle')
        polygon(
        (0, 0), # lower left
        (myShapeWidth/2, myShapeHeight), # top
        (myShapeWidth, 0)
        )
    
    
rect(0, 0, 100, 100)
    
    
triangle(0, 0, 100, 100)
translate(500, 500)
triangle(0, 0, 100, 100)
fill(0, 1, 0)
translate(0, -500)
triangle(100, 100, 200, 200)
