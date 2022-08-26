myPath = '../../assets/FONT_LICENSE.txt'
with open(myPath, 'r', encoding='utf-8') as myFile:
    myText = myFile.read()
    myParagraphs = myText.split('\n\n')
    myString = FormattedString('', font='JobClarendon-Regular', fontSize=50, lineHeight=50)

    for myParagraph in myParagraphs:
        myString.append(myParagraph+'\n\n', fill=(random(), random(), random()))
    m = 30
    myPageNumber = 1
    while myString:
        newPage('Letter')
        myString = textBox(myString, (m, m, width()-m*2, height()-m*2))
        text('Page '+str(myPageNumber), (m, m))
        myPageNumber += 1
    