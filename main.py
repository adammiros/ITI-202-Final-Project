import os
import string
from textblob import TextBlob

cwd = os.getcwd()







# Setup: Open TXT File, read data
file = open("sample.txt", mode="r")
text = file.read()

# Making everything lowercase to avoid duplicates
text = text.lower()

#Create Blob
blob = TextBlob(text)


#Close file
file.close()



subjectivity = blob.sentiment.subjectivity

print(subjectivity)


#Create empty dictionary
wordFrequencies = dict()


#Function to count occurances of words
def countwordFrequencies(data):
    #Split the data into words
    words = data.split()

    # Create a list of puncuation that can be checked against
    table = str.maketrans("", "", string.punctuation)

    #Perform the cleanup by checking against puncuation list in table variable
    words = [w.translate(table) for w in words]
    for word in words:
        if word in wordFrequencies:
            wordFrequencies[word] = wordFrequencies[word] + 1
                    
        else:
            wordFrequencies[word] = 1

    for key in list(wordFrequencies.keys()): 
        print(key, ":", wordFrequencies[key])




countwordFrequencies(text)



        

