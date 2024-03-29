from flask import Flask, request, render_template
import twitter
import cleanup
import analysis
import buildResponse
import log

text_file = "tweets.txt"


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    #Requesting the page
    if request.method == "GET":
        return render_template("home.html")

    #When user hits submit it runs the code inside this else if
    elif request.method == "POST":
        #On Submission get data from form
        username = request.form["username"]

        #Main function calls from other files occur here
        twitter.getFityLatestTweets(username)
        cleanup.cleanUpText(text_file)
        polarityScore, mood = analysis.getPolarity(text_file)

        response, emoji = buildResponse.buildResponse(polarityScore, mood, username)

        log.logQuery(username, polarityScore)

        #Used to test output before rendering results page
        print(response)
        print(emoji)

        #Rendering results page
        return render_template("result.html", response = response, emoji = emoji)


#Needed to start entire web application
if __name__ == "__main__":
    app.secret_key = 'Test'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)       