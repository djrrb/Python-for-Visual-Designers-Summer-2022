# set the font size so we can see stuff
fontSize(100)
# draw some text at (0, 0)
text('hello world', (0, 0))

# now reorient the canvas so that (0, 0) is now in the middle of the canvas
translate(width()/2, height()/2)

# now repeat the same line as above
# even though the text is still drawn at (0, 0), it will originate from the center of the canvas
text('hello world', (0, 0))