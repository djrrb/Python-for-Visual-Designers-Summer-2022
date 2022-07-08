# function(argument)
# hey i want to print something
print('hello world')

inch = 72
mm = 2.83465

#newPage(210*mm, 297*mm)
newPage('Tabloid')

fontSize(100)

font('BeatriceVariable-VF_Extrabold')

translate(0, height()-100)
text('hello world', (0, 0))

# fill(red, green, blue)
fill(
    1, # this is red
    0, # this is green
    0 # this is blue
)

text("what's up", (500, 500))#