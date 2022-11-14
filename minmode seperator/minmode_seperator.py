import os
import os.path

# # # # # FUNCTIONS # # # # #

def hasMinmode(line):

    found = False
    
    # _minmode
    for a in range(len(line)-7):
        
        nextEight = []
        for i in range(8):
            nextEight.append(line[a+i]) 
            
        if nextEight == list('_minmode'):
            found = True

    return found

def checkStructural(line):

    quoteCount = 0
    isStructural = 0

    for i in range(0, len(line)):
        if line[i] == '"':
            quoteCount += 1

    if quoteCount < 4:
        isStructural = 1

    return isStructural

def makeOutputPath(folder):

    filePath = 'output/' + folder
    if not os.path.isdir(filePath):
        os.makedirs(filePath)
        print(filePath + ' made')

    #return filePath

# # # # # MAIN # # # # #

files = os.listdir('input/')

makeOutputPath('base/')
makeOutputPath('RatzHud/')

for i in range(len(files)):

    fileLocation = 'input/' + files[i]

    resFile = open(fileLocation, 'r')
    resFileContents = resFile.readlines()
    resFile.close

    newMainLocation = 'base/' + files[i]
    mainOut = 'output/' + newMainLocation
    newMain = open(mainOut, 'w')

    newRatzLocation = 'RatzHud/' + 'RATZ' + files[i]
    ratzOut = 'output/' + newRatzLocation
    newRatz = open(ratzOut, 'w')

    rootOut = 'output/' + files[i]
    newRoot = open(rootOut, 'w')

    for a in range(len(resFileContents)):
        letters = []
        letters = list(resFileContents[a])

        minmodeFound = hasMinmode(letters)
        structural = checkStructural(letters)

        if structural == 1:
            newMain.write(resFileContents[a])
            newRatz.write(resFileContents[a])

        if structural == 0 and minmodeFound == 0:
            newMain.write(resFileContents[a])

        if structural == 0 and minmodeFound == 1:
            newRatz.write(resFileContents[a])

    newRoot.write('#base "' + newMainLocation + '"\n')
    newRoot.write('#base "' + newRatzLocation + '"')
    
    newRoot.close()
    newMain.close()
    newRatz.close()
        
input('Seperation complete. Press ENTER to exit')
    
