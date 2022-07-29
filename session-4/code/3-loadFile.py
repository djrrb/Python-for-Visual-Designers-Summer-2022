# filename as variable
myFileName = 'Business Cards - Sheet1.csv'

# open the file in read mode with UTF-8 encoding
# assign the file object to the variable name "myFile"
with open(myFileName, 'r', encoding="utf-8") as myFile:
    # we can read the file as a string
    myText = myFile.read()
    print('This file is', len(myText), 'characters long.')
    
with open(myFileName, 'r', encoding="utf-8") as myFile:
    # we can also read the file as lines
    myLines = myFile.readlines()
    print('This file is', len(myLines), 'lines long.')
    

