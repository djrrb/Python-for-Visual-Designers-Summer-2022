# define the image here
myImage = ImageObject('black-raspberries.jpg')
print(myImage)

# space between defining and drawing the image
#myImage.motionBlur(100, 90)
myImage.colorPosterize(3)
myImage.kaleidoscope()

myImage.sepiaTone()


# size stuff
myImageSize = myImage.size() # get the size
print(myImageSize) # print the size
myImageWidth, myImageHeight = myImage.size() # get the w and h as separate varaibles
print(width()/myImageWidth)
# scale the canvas so that the image’s width will fit
scale(width()/myImageWidth)



# draw the image
image(myImage, (0, 0))
