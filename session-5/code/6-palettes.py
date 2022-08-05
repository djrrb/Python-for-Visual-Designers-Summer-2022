from random import choice
# define a palette dictionary
# mapping palette name to another dictionary
# that sub dictionary maps foreground/background strings to color tuples

myColorPalettes = {
    'Aqua': {
        'foreground': (0, .9, 1, 1),
        'background': (0, .2, .5, 1)
        },
    
    'DarkMode': {
        'foreground': (1, 1, 1, 1),
        'background': (0, 0, 0, 1)
        },
        
    'LightMode': {
        'background': (1, 1, 1, 1),
        'foreground': (0, 0, 0, 1)
        }
    }

# loop through the palettes and draw something
for paletteName in myColorPalettes:
    thisPalette = myColorPalettes[paletteName]
    newPage()
    # call the background color for the fill and unpack it
    fill(*thisPalette['background'])
    rect(0, 0, width(), height())
    # call the foreground color for the fill and unpack it
    fill(*thisPalette['foreground'])
    oval(200, 200, 200, 200)

# now select a random palette
# and draw a background and some text using the palette
thisPalette = choice(list(myColorPalettes.values()))

newPage()
fill(*thisPalette['background'])
rect(0, 0, width(), height())
fill(*thisPalette['foreground'])
fontSize(100)
text('random palette', (100, 100))