myText = 'Hello world'

fontSize(100)
lineHeight(100)

# use text size to get the dimensions of the text as this font size in this font
print(textSize(myText))

# draw the text
text(myText, (0, 0))

# draw a rectangle the same dimensions as the text
rect(0, 100, *textSize(myText))