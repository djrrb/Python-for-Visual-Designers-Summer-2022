# import the CSV library
import csv

myInch = 72
myFileName = 'Business Cards - Sheet1.csv'

# open the file in read mode with utf-8 encoding as myFile
with open(myFileName, 'r', encoding="utf-8") as myFile:
    # read it as a CSV using the CSV reader object 
    myReader = csv.reader(myFile)
    # loop through the reader object
    for myRow in myReader:
        #myName = myRow[0]
        #myAddress = myRow[1]
        # assign each column to a variable name
        myName, myAddress, myPhone, myEmail = myRow
        
        # make a new page
        newPage(3.5*myInch, 2*myInch)
        # set the font size
        fontSize(12)
        # draw our text just above center
        text(myName, (width()/2, height()/2), align="center")
            
    

