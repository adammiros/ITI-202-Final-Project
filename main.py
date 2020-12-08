from nltk.util import pr
import twitter
import cleanup
import analysis

text_file = "tweets.txt"



twitter.getFityLatestTweets("")
cleanup.cleanUpText(text_file)
polarityScore, mood = analysis.getPolarity(text_file)



print(polarityScore)
print(mood)

        

