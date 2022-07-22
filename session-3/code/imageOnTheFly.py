# BezierPath, FormattedString
myImage = ImageObject()

with myImage:
    fill(1, 0, 0)
    oval(0, 0, 200, 200)
    fill(0)
    fontSize(100)
    text('hello universe', (0, 0))

myImage.motionBlur()
myImage.sepiaTone()

image(myImage, (0, 0))