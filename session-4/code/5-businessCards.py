# import the csv library
import csv

# set some constants
myInch = 72
myMargin = .25*myInch
myColWidth = 170
# where to read our data from
myFileName = 'Business Cards - Sheet1.csv'

mySaveIndividualFilesToggle = False

# open the file in read mode and utf-8 encoding
# asign the file object to the variable myFile
with open(myFileName, 'r', encoding="utf-8") as myFile:
    # make a special CSV reader object from the file object
    myReader = csv.reader(myFile)
    # now loop through the reader
    # use the enumerate function to get
    # the row number and the row contents at the same time
    for myRowNumber, myRow in enumerate(myReader):
        print(myRowNumber)
        # skip the first row using an if statement
        if myRowNumber == 0:
            continue
        # for all subsequent rows, set each column
        # to its own variable
        # so we can access it easily
        myName, myAddress, myPhone, myEmail = myRow
        
        # if we want to save individual files, start a new canvas
        # forget previous pages
        if mySaveIndividualFilesToggle:
            newDrawing()
        # make a new page
        newPage(3.5*myInch, 2*myInch)
        # move in to the margins        
        translate(myMargin, myMargin)
        # draw the logo
        # scale it down and move it
        # i just did this by eye
        with savedState():
            translate(-24, 23)
            scale(.07)
            image('https://i.pinimg.com/originals/9a/f6/5f/9af65fa681352b18598f825b40057630.png', (0, 0))
        # exit the saved state
        # move over so our text is to the right of the logo
        translate(60)
        
        # define a formatted string
        myString = FormattedString(
            myName,  # the text to draw
            font='Georgia Bold',  # font
            lineHeight=24, # leading
            fontSize=20, # font size
            fill=(1, 0, 0), # color
            #paragraphBottomSpacing=8
            )
            
        # add the address to the formatted string with different formatting
        myString.append(
            '\n\n'+myAddress+'\n\n', 
            font='Georgia', 
            fill=(0, 0, 0), 
            fontSize=10, 
            lineHeight=12
            )
        # finally add the email in italic
        myString.append(myEmail, font='Georgia Italic')
            
            
        # draw a text box the height of the page minus the margins
        myPageHeight = height()-myMargin*2

        # visualize the text box
        #fill(.9)
        #rect(0, 0, myColWidth, myPageHeight)
        
        # draw our formatted string into a text box
        textBox(myString, (0, 0, myColWidth, myPageHeight))
        
        # if we are saving individual files, do it for each row
        if mySaveIndividualFilesToggle:
            saveImage(myName+'-business-card.pdf')
# if we are saving them all at once, do it at the very end
# totaly dedented

if not mySaveIndividualFilesToggle:
    saveImage('allBusinessCards.pdf')
