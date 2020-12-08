import os
import string



def cleanUpText(fileToClean: str):
    
    #Opening file to read contents then closing
    file = open(fileToClean, mode="r", encoding="utf8")
    text = file.read()
    file.close()
    

    file = open(fileToClean, mode="w", encoding="utf8")


    

    for line in text:

        # Create a list of puncuation that can be checked against
        table = str.maketrans("", "", string.punctuation)

        #Perform the cleanup by checking against puncuation list in table variable then write it back to tweets.txt 
        cleanedText = [w.translate(table) for w in line]
        file.writelines(cleanedText)
        
    file.close()


#Usage: cleanUpText(NAME OF TXT File)

