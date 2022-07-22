# define an image object and “load” the image
# but do not draw it to canvas yet
myImage = ImageObject('black-raspberries.jpg')

# ask the image for its size
myImageSize = myImage.size()
# break apart its (w, h) size into width and height variables
myImageWidth, myImageHeight = myImage.size()
# i could also slice if I wanted, using [0] to get the first item
# myImageWidth = myImage.size()[0]

# figure out the amount we need to scale by
# in order to fit the full image onto the canvas
# divide canvas width by image width
myScaleAmount = width()/myImageWidth
print(myScaleAmount)

# apply the scale
scale(myScaleAmount)

# now finally draw the image to the canvas
# use our imageObject variable instead of the filename
image(myImage, (0, 0))