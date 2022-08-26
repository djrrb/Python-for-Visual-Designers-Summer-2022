# create an empty image
myImage = ImageObject()

# use the with statement to create a context for myImage
# and draw some stuff into it
with myImage:
    # everything at this indent will be part of the image
    rect(0, 0, 50, 50)
    font('Verdana', 150)
    fill(0, 1, 0)
    text('hello world', (0, 0))
    fill(1, 0, 0)
    oval(300, 300, 50, 50)

# do some filters
myImage.sepiaTone()
myImage.gaussianBlur()
# finally, draw the image to canvas
image(myImage, (0, 0))

