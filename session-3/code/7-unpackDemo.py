# my rect is a variable referring to a single tuple
# that tuple contains four items (x, y, w, h)
myRect = (0, 0, 100, 100)

# the rect() function needs this data as four separate items
# rect(0, 0, 100, 100)
# so we use the asterisk to “unpack” the tuple
# feeding each item from the tuple to rect()
# rather than the tuple itself
rect(*myRect)