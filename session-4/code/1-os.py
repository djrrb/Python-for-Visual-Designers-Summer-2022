import os
# get a base path, this is a relative path using ../ to go up one folder in the hierarchy
myBasePath = '../../session-3/challenges'
# get a destination folder
myDestFolder = 'sampleFolder'
# make the destination folder
os.mkdir(myDestFolder)

# loop through each file in our base path
for myFileName in os.listdir(myBasePath):
    # if it’s a ping
    if myFileName.endswith('.png'):
        # make a new drawing
        newDrawing()
        # get the path of this file by joining the basePath and fileName
        myPath = os.path.join(myBasePath, myFileName)
        # where do we want to save the exported gif file to
        # use a find and replace in the string
        myDestFileName = myFileName.replace('.png', '-export.gif')
        # get the full destination path by joining the destFolder and destFileName
        myDestPath = os.path.join(myDestFolder, myDestFileName)
        # get the image we are going to draw
        myImage = ImageObject(myPath)
        # unpack its size and feed it to newPage
        newPage(*myImage.size())
        # draw the image to canvas
        image(myImage, (0, 0))
        # save the image as the dest path
        saveImage(myDestPath)
        saveImage(myDestPath.replace('.gif', '.pdf'))
    