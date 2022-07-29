newPage(3.5*72, 2*72)

myWords = 'Hello World. Testing 123. These Are Some Small Caps.'

myMargin = 20

myString = FormattedString(
    myWords, 
    font="MinionPro-Regular", 
    fontSize = 14,
    lineHeight = 16,
    openTypeFeatures={'smcp': True}
    )

myTextBox = (
    myMargin,  # x
    myMargin,  # y 
    width()-myMargin*2,  # width
    height()-myMargin*2 # height
    )

textBox(myString, myTextBox)