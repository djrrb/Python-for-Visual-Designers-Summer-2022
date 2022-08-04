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
    
for paletteName in myColorPalettes:
    thisPalette = myColorPalettes[paletteName]
    newPage()
    ######

    fill(*thisPalette['background'])
    rect(0, 0, width(), height())
    fill(*thisPalette['foreground'])
    oval(200, 200, 200, 200)


