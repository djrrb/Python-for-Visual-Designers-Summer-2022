# define a shape without drawing it to canvas
myShape = BezierPath()

# add stuff to it
myShape.rect(0, 0, 100, 100)
myShape.oval(50, 50, 200, 200)
# make a random polygon 
myShape.polygon(
    (randint(0, 1000), randint(0, 1000)),
    (randint(0, 1000), randint(0, 1000)),
    (randint(0, 1000), randint(0, 1000)),
    (randint(0, 1000), randint(0, 1000)),
    (randint(0, 1000), randint(0, 1000)),
)

# all of these are part of the same shape object
# now draw it to canvas using drawPath()
drawPath(myShape)