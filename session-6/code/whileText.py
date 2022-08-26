# get the file path for our text file
myPath = '../../assets/FONT_LICENSE.txt'

# open the file
with open(myPath, 'r', encoding='utf-8') as myFile:
    # conver the file to text
    myText = myFile.read()
    # convert the text to string
    myString = FormattedString(
        myText, 
        font='Georgia', 
        fontSize=15, 
        lineHeight=20,
    )
    # set a margin and starting page number
    m = myMargin = 30
    myPageNumber = 1
    # do a while loop on myString
    # keep looping until myString is empty
    while myString:
        # make a new page
        newPage('Letter')
        # draw the text box, setting the overset text to overwrite myString
        # whittling myString down until it is empty
        myString = textBox(myString, (m, m, width()-m*2, height()-m*2))
        # draw a footer
        text('Page '+str(myPageNumber), (m, m))
        # augment the page number
        myPageNumber += 1
    