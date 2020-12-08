def buildResponse(score, mood, username):
    response = "It looks like " + username + " has a polarity score of " + str(score) + " meanining their overall vibe of all of their tweets is " + mood

    emoji = ""
    
    if (mood == "Positive"):
        emoji = "😀"
    elif (mood == "Neutral"):
        emoji =  "😶"
    elif (mood == "Negative"):
        emoji =  "🤬"
    
    return response, emoji