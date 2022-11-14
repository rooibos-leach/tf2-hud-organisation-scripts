import os
import os.path

# # # # # FUNCTIONS # # # # #

def hasName(line):

    found = False
    
    # name
    for a in range(len(line)-3):
        
        nextFour = []
        for i in range(4):
            nextFour.append(line[a+i]) 
            
        if nextFour == list('name'):
            found = True

    return found

files = os.listdir('input/')

for i in range(len(files)):

    fileLocation = 'input/' + files[i]

    fontFile = open(fileLocation, 'r')
    fontFileContents = fontFile.readlines()
    fontFile.close

    newFileOut = 'output/' + files[i]
    newFile = open(newFileOut, 'w')

    for a in range(len(fontFileContents)):
         
        letters = []
        letters = list(fontFileContents[a])

        nameFound = hasName(letters)

        if nameFound:
            newFile.write('\t\t\t\t' + '"name"' + '\t' + '"Homespun TT BRK"\n')

        else:
            newFile.write(fontFileContents[a])

    newFile.close()

input('Font conversion complete. Press "ENTER" to exit')





            
                        
    
