# define some text
myText = 'Happy Birthday'
# set a font
font('Times New Roman')

# to find the proportions
# set the font size and line height to 1
fontSize(1)
# use textSize() to get the width of the text at 1 point
# this is the ratio of width to height 
print(textSize(myText))
myMultiplier = textSize(myText)[0]

# get the font size we want by dividing the width we want to fit by the width/height ratio
myFontSize = width()/myMultiplier

# set the fontSize
fontSize(myFontSize)

# move up by the font descender
print(fontDescender())
translate(0, -fontDescender())
fill(.9)
# draw a retangle at the x height
rect(0, 0, width(), fontXHeight())

# draw the text
fill(0)
text(myText, (0, 0))



