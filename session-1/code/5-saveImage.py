# make a new page
newPage('A4Landscape')

# set the fill color
fill(1, 0, 0)
# also works with cmyk
#cmykFill(0, 1, 0, 0)

# now draw an oval the size of the canvas
oval(0, 0, width(), height())

# save our image in various formats
# this will go in the same folder as where the python script is saved
# if the script is unsaved, you’ll find it in your user folder /users/YourUserName
saveImage('red-oval.gif')
saveImage('red-oval.png')
saveImage('red-oval.pdf')
saveImage('red-oval.jpg')
