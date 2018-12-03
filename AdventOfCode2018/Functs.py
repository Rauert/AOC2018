def importFile(inFile):
    f = open(inFile, "r")
    lines = f.readlines()
    f.close()
    return lines
