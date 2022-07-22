# a “shortcut function” for making a new page with some default settings
def myNewPage():
    newPage()
    translate(200, 200)
    fill(1, 0, 0)
    font('Comic Sans MS', 150)

# using this function will create a new page and set a default canvas state
# simplifying our code
# and allowing us to make wide-reaching changes in a single place
myNewPage()
text('hello world', (0, 0))

# it will take effect each time a page is loaded
myNewPage()
text('page 2', (0, 0))

# if we don’t want the canvas settings, we don’t have to use it
newPage()
fontSize(100)
translate(0, -fontDescender())
text('page 3', (0, 0))

# but then we can use it again
myNewPage()
text('this is\npage 3', (0, 200))