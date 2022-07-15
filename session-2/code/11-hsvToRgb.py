# import the converter function to get RGB which drawbot likes
from colorsys import hsv_to_rgb

# convert HSV to RGB
myHue = .6
mySat = .8
myVal = 1

# print rgb values
print(hsv_to_rgb(myHue, mySat, myVal))

# split the resulting tuple into three variables
myR, myG, myB = hsv_to_rgb(myHue, mySat, myVal)
print(myR, myG, myB)

# set the fill
fill(myR, myG, myB)
rect(0, 0, 100, 100)

# or we can use the * to unpack the tuple directly into the fill function
fill(*hsv_to_rgb(myHue, mySat, myVal))
oval(200, 200, 100, 100)