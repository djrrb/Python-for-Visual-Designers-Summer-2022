# run 1-os.py first to get the sample folder that we will sort

# import os for basic operating system functions
import os
# import shutil for complex functions like copying and moving files
import shutil

# set a list of extensions that we want to sort
myExtensionList = ['.pdf', '.gif']

# 
myBasePath = 'sampleFolder'

# first, make a folder for each extension in our list if it doesn’t exist
for myExtension in myExtensionList:
    # call the folder myExtension but omit the first character, which is a period
    myPath = os.path.join(myBasePath, myExtension[1:])
    # if the path doesn’t exist
    if not os.path.exists(myPath):
        # make the folder
        os.mkdir(myPath)

# now loop through every file in the folder
for myFileName in os.listdir(myBasePath):
    # get the full path
    myPath = os.path.join(myBasePath, myFileName)
    # get this file’s extension
    myPathBase, myExtension = os.path.splitext(myPath)
    # if our file’s extension is in the extension list
    if myExtension in myExtensionList:
        # get the destination folder name (again removing the period at the beginning)
        myDestFolder = os.path.join(myBasePath, myExtension[1:])
        # get the full path
        myDestPath = os.path.join(myDestFolder, myFileName)
    print(myDestPath)
    # move the file from the original path to the new path
    shutil.move(myPath, myDestPath)
    