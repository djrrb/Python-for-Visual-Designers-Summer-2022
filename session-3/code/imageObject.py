myImage = ImageObject('black-raspberries.jpg')
print(myImage)
myImageSize = myImage.size()
print(myImageSize)
myImageWidth, myImageHeight = myImage.size()
print(width()/myImageWidth)

scale(width()/myImageWidth)
image(myImage, (0, 0))