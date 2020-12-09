from datetime import datetime

def logQuery(username, polarityResult):
    now = datetime.now()
    dateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")

    file = open("log.txt", mode="a", encoding="utf8")

    file.write("Query Time: " + str(dateAndTime) + " | Twitter Username: " + username + " | Polarity Result: " + str(polarityResult) + "\n") 