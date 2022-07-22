# rather than calling an external image
# let’s create an empty image and draw into it

# make an empty ImageObject
myImage = ImageObject()

# use the with statement to associate the indented code with myImage
with myImage:
    # set the fill to red
    fill(1, 0, 0)
    # draw a circle
    oval(0, 0, 200, 200)
    # set the fill to black
    fill(0)
    # draw some big text
    fontSize(100)
    text('hello universe', (0, 0))

# now we have an image with some stuff
# but we haven’t drawn it yet

# let’s apply some filters because why not
myImage.motionBlur()
myImage.sepiaTone()

# now let’s draw the image
image(myImage, (0, 0))