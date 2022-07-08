# define a custom function to convert hex values to rgb
# copied from
# https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    # ugh gotta add /255 to make it drawbot friendly colors
    return tuple(int(value[i:i + lv // 3], 16)/255 for i in range(0, lv, lv // 3))

# make a new page
newPage('A4Landscape')

# define a hex value we want to use as a variable
myHexValue = '#006699'
# now see what it looks like converted it to r, g, b
print(hex_to_rgb(myHexValue))

# in order to apply it to fill, we have to "unpack" the rgb tuple into its constituent parts
# use the asterisk to unpack the results of the function
fill(*hex_to_rgb(myHexValue))
# now draw an oval the size of the canvas
oval(0, 0, width(), height())
