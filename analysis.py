from textblob import TextBlob


def getPolarity(fileForAnalysis: str):
    mood = ""
    polarity_score = 0
    file = open(fileForAnalysis, mode="r", encoding="utf8")

    data = file.read()

    #Creating the blob object
    text = TextBlob(data)

    #Getting a polarity score
    polarity_score = text.sentiment.polarity

    if (polarity_score < 0):
        mood = "Negative"
    
    elif (polarity_score == 0):
        mood = "Neutral"

    elif (polarity_score > 0):
        mood = "Positive"


     
    return polarity_score, mood