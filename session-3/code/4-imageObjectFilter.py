# define the image here
myImage = ImageObject('black-raspberries.jpg')

# now we have space between defining and drawing the image
# ...
# ...
# let’s mess with the image first!
# filters at: https://drawbot.com/content/image/imageObject.html
myImage.motionBlur(100, 90)
myImage.colorPosterize(3)
myImage.kaleidoscope()

# let’s do that size calculation stuff
myImageWidth, myImageHeight = myImage.size() 
# scale the canvas so that the image’s width will fit
scale(width()/myImageWidth)


# now i am ready to draw the image to the canvas
image(myImage, (0, 0))
