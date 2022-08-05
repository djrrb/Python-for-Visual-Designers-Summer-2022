# here is a practical example of saved states

# we will navigate around the document and make it easy to change formatting and the go back

# define some variables
myMargin = 40
myPageNumber = 1
myTitle = 'The title page'
newPage('Letter')
# define the margin area
marginWidth = width()-myMargin*2
marginHeight = height()-myMargin*2


# save the state and move to the margin area
# that way we don’t have to calculate for margins anymore
with savedState():
    translate(myMargin, myMargin)
    rect(0, 0, marginWidth, marginHeight)

    # now save state and move to the canvas center
    with savedState():
        translate(marginWidth/2, marginHeight/2)
    
        # now save the state again
        # in this state, our stroke will be red and we will do some rotating
        with savedState():
            stroke(1, 0, 0)
            fill(None)
            for myNumber in range(20):
                rect(-150, -150, 300, 300)
                rotate(5)
        # dedent to undo the red stroke and rotating, we are just back to the center
        # now draw a title
        fill(1)
        font('Comic Sans MS', 35)
        text(myTitle, (0, 0), align="center")
    # dedent to leave the center, now we are back at the lower left of the margin
    # make a text box here
    fill(1)
    textBox('This is a descriptive paragraph! '*10, (0, 0, marginWidth, 50), align="center")

    # move to the upper left of the margin area to draw a logo
    # scale the canvas so the logo fits nicely
    with savedState():
        translate(0, marginHeight)
        fill(0, 1, 1)
        scale(.07)
        image('https://i.pinimg.com/originals/9a/f6/5f/9af65fa681352b18598f825b40057630.png', (250, -1500))
# dedent to exit the transformations, now we are back to the lower left
text('Page '+str(myPageNumber), (width()/2, 20))