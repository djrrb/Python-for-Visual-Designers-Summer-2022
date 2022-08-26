myImage = ImageObject()

with myImage:
    rect(0, 0, 50, 50)
    font('Verdana', 150)
    fill(0, 1, 0)
    text('hello world', (0, 0))
    fill(1, 0, 0)
    oval(300, 300, 50, 50)

myImage.sepiaTone()
myImage.gaussianBlur()
image(myImage, (0, 0))

