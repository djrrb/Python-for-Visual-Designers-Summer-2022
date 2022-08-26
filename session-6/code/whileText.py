myPath = '../../assets/FONT_LICENSE.txt'
with open(myPath, 'r', encoding='utf-8') as myFile:
    myText = myFile.read()
    myString = FormattedString(myText, font='JobClarendon-Regular', fontSize=50, lineHeight=50)
    m = 30
    myPageNumber = 1
    while myString:
        newPage('Letter')
        myString = textBox(myString, (m, m, width()-m*2, height()-m*2))
        text('Page '+str(myPageNumber), (m, m))
        myPageNumber += 1
    