# make a new page at a certain size
# can also take strings like 'Letter' or 'A4'
newPage(1500, 1000)

fontSize(100)
font('Georgia')

text('hello world', (0, 0))

# fill(red, green, blue)
fill(
    1, # this is red
    0, # this is green
    0 # this is blue
)
# now draw new text at 500, 500
text("what's up", (500, 500))#